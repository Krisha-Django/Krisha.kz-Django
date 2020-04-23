# Generated by Django 2.2 on 2020-04-23 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_', '0003_auto_20200423_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='is_super_man',
        ),
        migrations.AddField(
            model_name='myuser',
            name='role',
            field=models.IntegerField(choices=[(1, 'Admin'), (2, 'Customer')], default=2),
        ),
    ]
