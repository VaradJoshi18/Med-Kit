# Generated by Django 4.1 on 2022-09-04 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hos',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]
