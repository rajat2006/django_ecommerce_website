# Generated by Django 2.2.5 on 2019-11-12 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prproducts', '0002_auto_20191112_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=100, null=True),
        ),
    ]
