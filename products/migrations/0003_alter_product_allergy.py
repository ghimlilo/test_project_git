# Generated by Django 3.2.9 on 2021-11-13 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211113_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='allergy',
            field=models.ManyToManyField(through='products.Product_allergy', to='products.Allergy'),
        ),
    ]