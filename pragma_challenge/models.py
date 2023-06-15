from django.db import models

# Create your models here.




class Product(models.Model):
    product_ID=models.CharField(max_length=20,unique=True)
    product_name=models.CharField(max_length=30)
    product_category=models.CharField(max_length=30)
    product_price=models.DecimalField(max_digits = 6,decimal_places=2)


class Order(models.Model):
    Order_Id=models.IntegerField(primary_key=True, auto_created=True)   
    product_ID=models.ForeignKey(Product,on_delete=models.CASCADE)


