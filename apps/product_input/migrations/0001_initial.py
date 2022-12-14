# Generated by Django 4.1 on 2022-09-26 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier', '0001_initial'),
        ('product', '0004_rename_stock_load_productdetail_stock_loan'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInput',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificiacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('reference', models.CharField(max_length=50, unique=True)),
                ('quantity', models.PositiveSmallIntegerField(default=0)),
                ('in_wait', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
            ],
            options={
                'verbose_name': 'Entrada de producto',
                'verbose_name_plural': 'Entradas de producto',
                'ordering': ['-in_wait', '-id'],
            },
        ),
        migrations.CreateModel(
            name='InputDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificiacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('quantity', models.PositiveSmallIntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('product_input', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_input.productinput')),
            ],
            options={
                'verbose_name': 'Modelo base',
                'verbose_name_plural': 'Modelos base',
                'abstract': False,
            },
        ),
    ]
