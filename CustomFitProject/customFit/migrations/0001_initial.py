# Generated by Django 5.0.7 on 2024-07-21 10:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('manufacturer', models.CharField(max_length=50)),
                ('Capacity', models.FloatField()),
                ('calories', models.FloatField()),
                ('sodium', models.FloatField()),
                ('sugars', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customFit.foodcategory')),
            ],
        ),
    ]