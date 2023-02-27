# Generated by Django 4.1.7 on 2023-02-22 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Наименование')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=1000, verbose_name='Цена')),
                ('unit', models.CharField(blank=True, choices=[('л.', 'л.'), ('кг.', 'кг.'), ('кв/ч.', 'кв/ч.'), ('бр.', 'бр.'), ('мин.', 'мин.')], max_length=10, null=True, verbose_name='Мярка')),
                ('quantity', models.DecimalField(blank=True, decimal_places=3, default=1, max_digits=10, null=True, verbose_name='Количество')),
                ('comment', models.TextField(blank=True, default=None, max_length=200, null=True, verbose_name='Забележка')),
            ],
        ),
    ]
