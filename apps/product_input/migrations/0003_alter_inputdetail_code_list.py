# Generated by Django 4.1.1 on 2022-10-15 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_input', '0002_alter_inputdetail_options_inputdetail_code_list_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputdetail',
            name='code_list',
            field=models.CharField(default='', max_length=10000),
        ),
    ]
