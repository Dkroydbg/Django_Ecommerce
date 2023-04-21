# Generated by Django 4.2 on 2023-04-14 09:44

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
                ('product_name', models.CharField(max_length=50)),
                ('product_price', models.IntegerField(default=0)),
                ('product_image', models.ImageField(upload_to='products/')),
                ('product_description', models.CharField(max_length=200)),
            ],
        ),
    ]
