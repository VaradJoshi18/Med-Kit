# Generated by Django 4.1 on 2022-10-13 05:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0004_alter_timeline_datetime_alter_timeline_doc_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeline',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 5, 13, 16, 26331, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='timeline_doc',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 5, 13, 16, 26331, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='timeline_pharma',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 13, 5, 13, 16, 26331, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
