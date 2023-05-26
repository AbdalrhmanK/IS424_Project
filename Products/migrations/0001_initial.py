# Generated by Django 4.2.1 on 2023-05-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pName', models.CharField(max_length=20)),
                ('nameShop', models.CharField(max_length=20)),
                ('shopContact', models.CharField(max_length=20)),
                ('pAmount', models.FloatField(max_length=10)),
                ('description', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
