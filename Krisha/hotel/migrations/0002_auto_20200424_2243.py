# Generated by Django 2.2.12 on 2020-04-24 22:43

from django.db import migrations, models
import django.db.models.deletion
import hotel.validators


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hotels', to='city.City', unique=True),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='contact',
            field=models.CharField(max_length=12, unique=True, validators=[hotel.validators.validated_contact]),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='name',
            field=models.CharField(max_length=100, unique=True, validators=[hotel.validators.validate_name]),
        ),
    ]
