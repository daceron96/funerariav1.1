# Generated by Django 4.1 on 2022-09-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_stock_load_productdetail_stock_loan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='code_list',
            field=models.CharField(blank=True, default=[], max_length=500),
        ),
    ]