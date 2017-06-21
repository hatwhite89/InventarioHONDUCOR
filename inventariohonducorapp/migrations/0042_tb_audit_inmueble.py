# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-19 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventariohonducorapp', '0041_auto_20170617_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='tb_audit_inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TableName', models.CharField(max_length=45)),
                ('Operation', models.CharField(max_length=1)),
                ('OldValue', models.TextField(blank=True, null=True)),
                ('NewValue', models.TextField(blank=True, null=True)),
                ('UpdateDate', models.DateField()),
                ('UserName', models.CharField(max_length=45)),
            ],
        ),
    ]
