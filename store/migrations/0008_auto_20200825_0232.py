# Generated by Django 3.1 on 2020-08-25 02:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20200821_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'First name must be greater than 1 character')]),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(2, 'last name must be greater than 1 character')]),
        ),
    ]
