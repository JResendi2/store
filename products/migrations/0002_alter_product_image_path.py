# Generated by Django 5.0.1 on 2024-06-15 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_path',
            field=models.FileField(default='', upload_to='img-products'),
        ),
    ]
