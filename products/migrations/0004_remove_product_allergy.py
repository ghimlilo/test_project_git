# Generated by Django 3.2.9 on 2021-11-13 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_allergy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='allergy',
        ),
    ]
