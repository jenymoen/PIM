# Generated by Django 5.1.4 on 2025-03-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pimApp', '0005_suppliers'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopifySettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
            ],
        ),
    ]
