# Generated by Django 2.2.12 on 2020-04-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='card_number',
            field=models.CharField(default=0, max_length=16),
        ),
    ]
