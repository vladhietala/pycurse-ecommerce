# Generated by Django 4.0.2 on 2022-02-25 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_order_options_alter_order_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ('-created_at',), 'verbose_name': 'Order item', 'verbose_name_plural': 'Order items'},
        ),
    ]
