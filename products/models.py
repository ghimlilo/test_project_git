from django.db import models
from django.db.models.deletion import CASCADE


class Menu(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'menus'

class Category(models.Model):
    name = models.CharField(max_length=20)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    name     = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    class Meta:
        db_table = 'products'

class Allergy(models.Model):
    name     = models.CharField(max_length=20)
  
    class Meta:
        db_table = 'allergen'

class Product_allergy(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    allergy = models.ForeignKey('Allergy', on_delete=models.CASCADE)
    class Meta:
        db_table = 'products_allergen'

class Image(models.Model):
    image_url = models.URLField(max_length=200) 
    
    product = models.ForeignKey('Product', on_delete=CASCADE)
    class Meta:
        db_table = "images"   
