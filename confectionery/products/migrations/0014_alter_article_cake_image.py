# Generated by Django 4.1.7 on 2023-02-26 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_alter_article_cake_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cake_image',
            field=models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/', verbose_name='Снимка'),
        ),
    ]