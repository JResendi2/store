# Generated by Django 5.0.1 on 2024-06-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_path',
            field=models.ImageField(default='', upload_to='img-products'),
        ),
    ]