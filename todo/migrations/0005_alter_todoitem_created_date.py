# Generated by Django 4.1 on 2022-09-30 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todoitem_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 30, 16, 59, 12, 719134, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
