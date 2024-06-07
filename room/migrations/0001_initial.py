# Generated by Django 5.0.6 on 2024-06-07 16:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=120, verbose_name='Name')),
                ('type', models.CharField(choices=[('focus', 'FOCUS Room'), ('team', 'TEAM Room'), ('conference', 'CONFERENCE Room')], default='focus', max_length=60, verbose_name='Type')),
                ('capacity', models.IntegerField(verbose_name='Capacity')),
            ],
            options={
                'verbose_name': 'Room',
                'verbose_name_plural': 'Rooms',
            },
        ),
        migrations.CreateModel(
            name='RoomBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('booked', models.BooleanField(default=False)),
                ('resident', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room_bookings', to='room.resident')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_bookings', to='room.room')),
            ],
            options={
                'verbose_name': 'Room Book',
                'verbose_name_plural': 'Room Books',
            },
        ),
        migrations.AddConstraint(
            model_name='roombooking',
            constraint=models.CheckConstraint(check=models.Q(('start__gte', models.F('end')), _negated=True), name='start_before_end'),
        ),
    ]