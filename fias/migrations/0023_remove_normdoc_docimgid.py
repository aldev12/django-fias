# Generated by Django 2.0 on 2020-04-06 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fias', '0022_auto_20200401_0156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='normdoc',
            name='docimgid',
        ),
    ]