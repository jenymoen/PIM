# Generated by Django 5.1.4 on 2025-05-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimApp', '0007_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
