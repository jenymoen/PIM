from django.db import models


class Product(models.Model):
    sku = models.CharField(max_length=20 ,blank=False, null=False)
    product_name = models.CharField(max_length=20 ,blank=False, null=False)
    description = models.CharField(max_length=20 ,blank=False, null=False)
    product_image = models.ImageField()
    manufacturer = models.CharField(max_length=20 ,blank=False, null=False)
    weight = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    barcode = models.IntegerField()
    #status_enriched = 

    def __str__(self):
        return self.product_name


