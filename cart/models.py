from django.db import models


# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    photo = models.ImageField(upload_to='product_image/', default="")

    def __str__(self):
        return self.name


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=12, blank=False)
    add1 = models.CharField(max_length=50)
    add2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    code = models.IntegerField()

    def __str__(self):
        return self.f_name


class Cart(models.Model):
    prod_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=50)
    prod_price = models.IntegerField()
    prod_qty = models.IntegerField()

    def __str__(self):
        return self.prod_name
