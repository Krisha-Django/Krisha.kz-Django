# Generated by Django 2.2.12 on 2020-04-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0002_auto_20200423_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='card_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]