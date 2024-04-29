# Generated by Django 4.1 on 2022-10-13 05:15

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0009_doc_image'),
        ('chat', '0005_alter_chat_date_alter_chat_senderid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 10, 13, 5, 15, 35, 172278, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='chat',
            name='receiverId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='register.user', to_field='username'),
        ),
    ]
