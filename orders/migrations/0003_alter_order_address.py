# Generated by Django 5.1.3 on 2024-12-17 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_address_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
