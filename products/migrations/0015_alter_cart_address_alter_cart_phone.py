# Generated by Django 4.2.3 on 2023-08-03 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_alter_cart_address_alter_cart_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='address',
            field=models.CharField(blank=True, default='пусто', max_length=128),
        ),
        migrations.AlterField(
            model_name='cart',
            name='phone',
            field=models.CharField(blank=True, default='пусто', max_length=13),
        ),
    ]
