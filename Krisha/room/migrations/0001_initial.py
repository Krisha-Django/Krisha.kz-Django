# Generated by Django 2.2.12 on 2020-04-23 13:13

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(max_length=10000)),
                ('room_description', models.CharField(default='Description', max_length=300)),
                ('type', models.IntegerField(choices=[(1, 'Single'), (2, 'Double'), (3, 'Triple'), (4, 'Quad')], default=1)),
                ('status', models.BooleanField(default=False)),
                ('price', models.IntegerField(default=10000)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='hotel.Hotel')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
            managers=[
                ('rooms_by_types', django.db.models.manager.Manager()),
            ],
        ),
    ]
