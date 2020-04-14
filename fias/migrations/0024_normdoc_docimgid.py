# Generated by Django 2.0 on 2020-04-06 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fias', '0023_remove_normdoc_docimgid'),
    ]

    operations = [
        migrations.AddField(
            model_name='normdoc',
            name='docimgid',
            field=models.UUIDField(blank=True, null=True, verbose_name='Идентификатор образа (внешний ключ)'),
        ),
    ]
