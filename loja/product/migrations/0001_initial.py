# Generated by Django 4.0.2 on 2022-02-22 04:03

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
                ('product_name', models.CharField(max_length=100)),
                ('short_description', models.TextField(max_length=255)),
                ('long_description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('slug', models.SlugField(max_length=30, unique=True)),
                ('mktg_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('promo_mktg_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('type', models.CharField(choices=[('V', 'Variable'), ('S', 'Simple')], default='V', max_length=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]