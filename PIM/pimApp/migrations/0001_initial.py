# Generated by Django 5.1.4 on 2024-12-16 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(max_length=20)),
                ('product_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('product_image', models.ImageField(upload_to='')),
                ('manufacturer', models.CharField(max_length=20)),
                ('weight', models.IntegerField()),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('barcode', models.IntegerField()),
            ],
        ),
    ]
