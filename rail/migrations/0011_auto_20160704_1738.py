# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rail', '0010_auto_20160704_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'permissions': (('can_add_album', 'Can add album'), ('can_view_album', 'Can view album'))},
        ),
    ]
