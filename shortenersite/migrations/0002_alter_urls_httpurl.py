# Generated by Django 4.0.3 on 2022-03-02 12:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortenersite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urls',
            name='httpurl',
            field=models.URLField(validators=[django.core.validators.URLValidator], verbose_name='Полная ссылка'),
        ),
    ]
