# Generated by Django 4.0.6 on 2022-11-07 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_item_discount_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(blank=True, choices=[('new', 'new'), ('sale', 'sale')], max_length=4, null=True),
        ),
    ]
