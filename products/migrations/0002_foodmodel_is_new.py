# Generated by Django 4.2.3 on 2023-07-27 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodmodel',
            name='is_new',
            field=models.BooleanField(default=True, verbose_name='is new'),
        ),
    ]