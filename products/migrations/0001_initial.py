# Generated by Django 5.1.3 on 2024-11-29 13:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Список категорий',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Параметр',
                'verbose_name_plural': 'Список параметров',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Список магазинов',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Список продуктов',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('price_rrc', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infos', to='products.product')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='infos', to='products.shop')),
            ],
            options={
                'verbose_name': 'Информация о продукте',
                'verbose_name_plural': 'Список информации о продуктах',
                'ordering': ('product',),
            },
        ),
        migrations.CreateModel(
            name='ProductParameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=150)),
                ('parameter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='products.parameter')),
                ('product_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_parameters', to='products.productinfo')),
            ],
            options={
                'verbose_name': 'Параметр продукта',
                'verbose_name_plural': 'Список параметров продуктов',
                'ordering': ('product_info',),
            },
        ),
        migrations.AddField(
            model_name='category',
            name='shops',
            field=models.ManyToManyField(related_name='categories', to='products.shop'),
        ),
    ]