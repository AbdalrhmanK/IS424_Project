# Generated by Django 4.2.1 on 2023-05-27 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0016_remove_product_pamount22_product_pamount0'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='pAmount0',
            new_name='pAmount00',
        ),
    ]
