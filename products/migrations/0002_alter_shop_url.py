# Generated by Django 5.1.3 on 2024-12-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
