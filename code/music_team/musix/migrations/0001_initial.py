# Generated by Django 4.2 on 2024-09-15 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', max_length=16, unique=True)),
                ('host', models.CharField(max_length=60, unique=True)),
                ('guest_can_pause', models.BooleanField(default=False)),
                ('votes_to_skip', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
