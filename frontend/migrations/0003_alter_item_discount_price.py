# Generated by Django 5.0.6 on 2024-07-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_item_discount_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='discount_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
