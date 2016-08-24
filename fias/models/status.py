#coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.db import models

__all__ = [
    'ActStat', 'CenterSt', 'CurentSt',
    'EstStat', 'HSTStat', 'IntvStat',
    'OperStat', 'StrStat'
]


class ActStat(models.Model):
    """
    Информация по статусу актуальности в БД ФИАС
    """
    class Meta:
        app_label = 'fias'
        verbose_name = 'Статус актуальности ФИАС'
        verbose_name_plural = 'Статусы актуальности ФИАС'

    actstatid = models.PositiveIntegerField(primary_key=True, verbose_name='Идентификатор статуса (ключ)')
    name = models.CharField('Наименование', max_length=100)


class CenterSt(models.Model):
    """
    Информация по статусу центра в БД ФИАС
    """
    class Meta:
        app_label = 'fias'
        verbose_name = 'Статус центра'
        verbose_name_plural = 'Статусы центров'

    centerstid = models.PositiveIntegerField(primary_key=True, verbose_name='Идентификатор статуса')
    name = models.CharField('Наименование', max_length=100)


class CurentSt(models.Model):
    """
    Информация по статусу актуальности КЛАДР 4.0 в БД ФИАС
    """
    class Meta:
        app_label = 'fias'
        verbose_name = 'Статус актуальности КЛАДР 4.0'
        verbose_name_plural = 'Статусы актуальности КЛАДР 4.0'

    curentstid = models.PositiveIntegerField(primary_key=True, verbose_name='Идентификатор статуса (ключ)')
    name = models.CharField('Наименование', max_length=100)


class EstStat(models.Model):
    """
    Информация по признакам владения в БД ФИАС
    """
    class Meta:
        app_label = 'fias'
        verbose_name = 'Признак владения'
        verbose_name_plural = 'Признаки владения'

    eststatid = models.PositiveIntegerField(primary_key=True, verbose_name='Признак владения')
    name = models.CharField('Наименование', max_length=20)
    shortname = models.CharField('Краткое наименование', max_length=20, blank=True, null=True)


class HSTStat(models.Model):
    """
    Информация по статусу состояния домов  в БД ФИАС
    """
    class Meta:
        app_label = 'fias'
        verbose_name = 'Статус состояния домов'
        verbose_name_plural = 'Статусы состояния домов'

    housestid = models.PositiveIntegerField(primary_key=True, verbose_name='Идентификатор статуса')
    name = models.CharField('Наименование', max_length=60)


class IntvStat(models.Model):
    """
    Информация по статусу интервалов домов в БД ФИАС
    """
    class Meta:
        app_label = 'fias'
        verbose_name = 'Статус интервала домов'
        verbose_name_plural = 'Статусы интервалов домов'

    intvstatid = models.PositiveIntegerField(primary_key=True,
                                             verbose_name='Идентификатор статуса (обычный, четный, нечетный)')
    name = models.CharField('Наименование', max_length=60)


class OperStat(models.Model):
    """
    Информация по статусу действия в БД ФИАС
    """
    class Meta:
        app_label = 'fias'
        verbose_name = 'Статус действия'
        verbose_name_plural = 'Статусы действия'

    operstatid = models.PositiveIntegerField(primary_key=True, verbose_name='Идентификатор статуса (ключ)')
    name = models.CharField('Наименование', max_length=100)


class StrStat(models.Model):
    """
    Информация по признакам строения в БД ФИАС
    """
    class Meta:
        app_label = 'fias'
        verbose_name = 'Признак строения'
        verbose_name_plural = 'Признаки строения'

    strstatid = models.PositiveIntegerField('Признак строения', primary_key=True)
    name = models.CharField('Наименование', max_length=20)
    shortname = models.CharField('Краткое наименование', max_length=20, blank=True, null=True)
