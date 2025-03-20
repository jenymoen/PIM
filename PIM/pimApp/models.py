from django.db import models
import requests, json

class Collections(models.Model):
    collection_name = models.CharField(max_length=20 ,blank=False, null=False)
    collection_description = models.CharField(max_length=20 ,blank=False, null=False)
    collection_image = models.ImageField()
    

    def __str__(self):
        return self.collection_name


class Product(models.Model):
    sku = models.CharField(max_length=20 ,blank=False, null=False)
    product_name = models.CharField(max_length=20 ,blank=False, null=False)
    description = models.CharField(max_length=20 ,blank=False, null=False)
    product_image = models.ImageField()
    manufacturer = models.CharField(max_length=20 ,blank=False, null=False)
    weight = models.IntegerField(blank=True, null=False)
    length = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    barcode = models.IntegerField()
    collection_products = models.ManyToManyField(Collections)
    
    #status_enriched = 

    def push_to_shopify(self):
        url = "https://santiccycling.myshopify.com/admin/api/2024-07/products.json"
        headers = {
            'Content-Type': 'application/json',
            'X-Shopify-Access-Token': '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'
        }
        data = {
            "product": {
                "title": self.product_name,
                "body_html": self.description,
                "vendor": self.manufacturer,
                "product_type": "Hard Good",
                "images": [
                    {
                        "src": ""
                    }
                ],
                "variants": [
                    {
                        "sku": self.sku,
                        "weight": self.weight,
                        "weight_unit": "g",
                        "inventory_management": "shopify",
                        "inventory_quantity": 1,
                        "price": 10.00
                    }
                ]
            }
        }
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 201:
            print("Product pushed to Shopify successfully")
        else:
            print(f"Failed to push product to Shopify. Response: {response.status_code} - {response.text}")
    

    def __str__(self):
        return self.product_name




