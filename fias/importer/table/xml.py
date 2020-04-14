# coding: utf-8
from __future__ import unicode_literals, absolute_import

import datetime
from lxml import etree

from django.db import models
from fias.fields import UUIDField
from .table import BadTableError, Table, TableIterator, ParentLookupException

_bom_header = b'\xef\xbb\xbf'


class XMLIterator(TableIterator):

    def __init__(self, fd, model):
        super(XMLIterator, self).__init__(fd=fd, model=model)

        self.related_fields = dict({
            (f.name, f.remote_field.model) for f in self.model._meta.get_fields()
            if f.one_to_one or f.many_to_one
        })

        self.uuid_fields = dict({
            (f.name, f) for f in self.model._meta.get_fields()
            if isinstance(f, UUIDField)
        })

        self.date_fields = dict({
            (f.name, f) for f in self.model._meta.get_fields()
            if isinstance(f, models.DateField)
        })

        self.int_fields = dict({
            (f.name, f) for f in self.model._meta.get_fields()
            if isinstance(f, models.IntegerField)
        })

        self._context = etree.iterparse(self._fd)

    def format_row(self, row):
        for key, value in row.items():
            key = key.lower()
            if key in self.uuid_fields:
                yield (key, value or None)
            elif key in self.date_fields:
                if value == '' or value is None:
                    yield (key, None)
                else:
                    try:
                        _date = datetime.datetime.strptime(value, "%Y-%m-%d").date()
                    except ValueError:
                        _date = datetime.datetime.strptime(value, "%d.%m.%y %H:%M:%S").date()
                    yield (key, _date)
            elif key in self.related_fields:
                if value == '':
                    value = None
                yield ('{0}_id'.format(key), value)
            elif key in self.int_fields:
                if value == '':
                    value = None
                yield (key, value)
            else:
                yield (key, value)

    def get_next(self):
        event, row = next(self._context)
        item = self.process_row(row)
        row.clear()
        while row.getprevious() is not None:
            del row.getparent()[0]

        return item


class XMLTable(Table):
    iterator = XMLIterator

    def __init__(self, filename, **kwargs):
        super(XMLTable, self).__init__(filename=filename, **kwargs)

    def rows(self, tablelist):
        if self.deleted:
            return []

        xml = self.open(tablelist=tablelist)

        # workaround for XMLSyntaxError: Document is empty, line 1, column 1
        bom = xml.read(3)
        if bom != _bom_header:
            xml = self.open(tablelist=tablelist)
        else:
            #log.info('Fixed wrong BOM header')
            pass

        try:
            return self.iterator(xml, self.model)
        except etree.XMLSyntaxError as e:
            raise BadTableError('Error occured during opening table `{0}`: {1}'.format(self.name, str(e)))
