# Generated by Django 5.0.4 on 2024-07-17 09:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.vehicle')),
            ],
        ),
    ]
