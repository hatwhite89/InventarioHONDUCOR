# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventariohonducorapp', '0022_auto_20170608_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='tb_admin_inmueble',
            name='estado_admin_inmueble',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_articulo',
            name='estado_articulo',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_categoria_art',
            name='estado_cat_art',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_detallearticulo',
            name='estado_det_art',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_entrada',
            name='estado_entrada',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_incidenciaarticulo',
            name='estado_inc_art',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_incidenciamobiliario',
            name='estado_inci_mobi',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_incidenciavehiculo',
            name='estado_inci_vehi',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_inmueble',
            name='estado_inmueble',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_mobiliariodevuelto',
            name='estado_md',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_mobiliarioprestado',
            name='estado_mp',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_salida',
            name='estado_salida',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_vehiculo',
            name='estado_vehi',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_vehiculoasignado',
            name='estado_vehi_asig',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='tb_vehiculodescargado',
            name='estado_vehi_des',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
