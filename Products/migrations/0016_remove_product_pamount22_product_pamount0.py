# Generated by Django 4.2.1 on 2023-05-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0015_alter_product_pamount22'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='pAmount22',
        ),
        migrations.AddField(
            model_name='product',
            name='pAmount0',
            field=models.DecimalField(decimal_places=2, default=10.0, max_digits=5),
            preserve_default=False,
        ),
    ]
