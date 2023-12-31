# Generated by Django 4.2.2 on 2023-07-21 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_alter_card_type_delete_types'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catetype', models.CharField(max_length=50, verbose_name='Tür')),
            ],
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appMy.type', verbose_name='Tür'),
        ),
    ]
