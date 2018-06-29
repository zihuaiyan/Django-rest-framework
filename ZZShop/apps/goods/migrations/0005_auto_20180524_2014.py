# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 20:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_auto_20180524_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.CharField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], default=1, help_text='类目级别', max_length=30, verbose_name='类目级别'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='is_tab',
            field=models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航'),
        ),
        migrations.AlterField(
            model_name='goodscategory',
            name='parent_category',
            field=models.ForeignKey(blank=True, help_text='父类目级别', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='goods.GoodsCategory', verbose_name='父类目级别'),
        ),
    ]