# Generated by Django 4.0.6 on 2023-03-22 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0023_alter_item_discount_price_alter_item_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('shirt', 'shirt'), ('sport', 'sport'), ('outwears', 'outwears')], max_length=10),
        ),
    ]