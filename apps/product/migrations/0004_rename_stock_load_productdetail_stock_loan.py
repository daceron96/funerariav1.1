# Generated by Django 4.1 on 2022-09-10 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_productdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productdetail',
            old_name='stock_load',
            new_name='stock_loan',
        ),
    ]