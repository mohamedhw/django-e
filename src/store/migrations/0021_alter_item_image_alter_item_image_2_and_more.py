# Generated by Django 4.0.6 on 2023-01-07 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_item_image_2_alter_item_image_3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='item_pic'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_2',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='item_pic'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_3',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='item_pic'),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_4',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='item_pic'),
        ),
    ]
