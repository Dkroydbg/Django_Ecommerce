from django.db import models
from .category import Category


class Product(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    product_image = models.ImageField(upload_to='Uploads/products/')
    product_description = models.CharField(max_length=200,default='',null=True,blank=True)


    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)   
        else:
            return Product.get_all_products()
