# Generated by Django 2.0 on 2020-04-01 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fias', '0021_auto_20200326_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='buildnum',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер корпуса'),
        ),
        migrations.AlterField(
            model_name='house',
            name='strucnum',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер строения'),
        ),
    ]
