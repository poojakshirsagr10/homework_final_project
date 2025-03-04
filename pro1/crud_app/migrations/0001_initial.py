# Generated by Django 5.0.3 on 2024-03-25 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_price', models.IntegerField()),
                ('product_quan', models.IntegerField()),
                ('delivery_address', models.CharField(max_length=20)),
                ('payment_mode', models.CharField(choices=[('ON', 'ONLINE'), ('COD', 'Cash On Delievery')], max_length=3)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
