# Generated by Django 4.1 on 2022-09-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_appointment_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]
