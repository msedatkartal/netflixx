# Generated by Django 4.2.2 on 2023-07-21 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0007_rename_type_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(max_length=50, null=True, verbose_name='Tür'),
        ),
        migrations.DeleteModel(
            name='Types',
        ),
    ]
