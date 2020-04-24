# Generated by Django 2.2.12 on 2020-04-24 22:40

from django.db import migrations, models
import room.validators


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_number',
            field=models.CharField(default=0, max_length=5, unique=True, validators=[room.validators.validated_room_number]),
        ),
    ]
