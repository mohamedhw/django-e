# Generated by Django 4.0.6 on 2023-01-07 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_item_image_2_item_image_3_item_image_4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_4',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='item_pic'),
        ),
    ]
