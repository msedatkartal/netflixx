# Generated by Django 4.2.2 on 2023-07-28 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0011_alter_card_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='like',
            field=models.BooleanField(default=False, verbose_name='Favori Mi?'),
        ),
    ]