# Generated by Django 4.2.1 on 2023-05-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0023_product_pamount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='nameShop',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='pName',
            field=models.CharField(default='None', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='shopContact',
            field=models.CharField(default='None', max_length=20),
        ),
    ]