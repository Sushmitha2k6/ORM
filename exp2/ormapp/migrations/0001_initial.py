# Generated by Django 5.1.7 on 2025-04-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('userid', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('mobileno', models.IntegerField()),
                ('mailid', models.EmailField(max_length=254)),
                ('moviename', models.CharField(max_length=50)),
                ('noofseats', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
