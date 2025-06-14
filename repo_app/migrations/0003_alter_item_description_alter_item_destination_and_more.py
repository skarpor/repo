# Generated by Django 4.2.19 on 2025-02-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo_app', '0002_alter_brand_description_alter_item_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='描述'),
        ),
        migrations.AlterField(
            model_name='item',
            name='destination',
            field=models.TextField(blank=True, null=True, verbose_name='去向'),
        ),
        migrations.AlterField(
            model_name='item',
            name='usage',
            field=models.TextField(blank=True, null=True, verbose_name='用途'),
        ),
    ]
