# Generated by Django 3.0.5 on 2020-05-07 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_customuser_verified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='Verified',
        ),
        migrations.AddField(
            model_name='customuser',
            name='verified',
            field=models.NullBooleanField(default=False, help_text='Подписаться на рассылку сообщений?'),
        ),
    ]
