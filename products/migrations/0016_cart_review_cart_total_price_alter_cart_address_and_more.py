# Generated by Django 4.2.3 on 2023-08-03 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_cart_address_alter_cart_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='review',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='address',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='cart',
            name='phone',
            field=models.CharField(blank=True, max_length=13),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(choices=[('order', 'Заказ'), ('processing', 'Обработка'), ('cooking', 'Готовка'), ('shipped', 'Отправлена'), ('delivered', 'Доставлена'), ('not active', 'Не активен')], default='order', max_length=20),
        ),
    ]
