# Generated by Django 4.2.3 on 2023-07-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_foodmodel_description_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodmodel',
            name='description',
        ),
        migrations.RemoveField(
            model_name='foodmodel',
            name='description_image',
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='ru_description',
            field=models.TextField(null=True, verbose_name='ru_description'),
        ),
        migrations.AddField(
            model_name='foodmodel',
            name='uz_description',
            field=models.TextField(null=True, verbose_name='uz_description'),
        ),
    ]
