# Generated by Django 4.1.1 on 2022-10-03 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_output', '0002_alter_ouputdetail_options_alter_outputtype_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoutput',
            name='invoice_number',
            field=models.CharField(max_length=50),
        ),
    ]
