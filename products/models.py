from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=255, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_path = models.ImageField(default="", upload_to="img-products")