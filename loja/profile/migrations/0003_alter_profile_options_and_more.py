# Generated by Django 4.0.2 on 2022-02-25 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_alter_profile_address_complement'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address_city',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address_complement',
            new_name='complement',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address_neighborhood',
            new_name='neighborhood',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address_number',
            new_name='number',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address_cep',
            new_name='postalcode',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='address_state',
            new_name='state',
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(verbose_name='birth date'),
        ),
    ]