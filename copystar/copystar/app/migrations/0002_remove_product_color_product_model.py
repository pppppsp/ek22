# Generated by Django 4.1.7 on 2023-05-22 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.AddField(
            model_name='product',
            name='model',
            field=models.CharField(default=1, max_length=50, verbose_name='Модель'),
            preserve_default=False,
        ),
    ]
