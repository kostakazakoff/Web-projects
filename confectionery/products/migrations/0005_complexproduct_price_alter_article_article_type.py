# Generated by Django 4.1.7 on 2023-02-24 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_article_article_type_alter_complexproduct_unit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complexproduct',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, editable=None, max_digits=1000, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='article',
            name='article_type',
            field=models.CharField(blank=True, choices=[('cake', 'Торта'), ('peace_of_cake', 'Паста'), ('other', 'Други')], default='cake', max_length=100, verbose_name='Вид'),
        ),
    ]
