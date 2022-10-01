# Generated by Django 4.1 on 2022-09-10 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0001_initial'),
        ('product', '0002_alter_productcategory_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de modificiacion')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de eliminación')),
                ('code_list', models.CharField(blank=True, default='', max_length=500)),
                ('stock_cellar', models.PositiveSmallIntegerField(default=0)),
                ('stock_wait', models.PositiveSmallIntegerField(default=0)),
                ('stock_load', models.PositiveSmallIntegerField(default=0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='supplier.supplier')),
            ],
            options={
                'verbose_name': 'Detalle de producto',
                'verbose_name_plural': 'Detalles de producto',
                'ordering': ['pk'],
            },
        ),
    ]
