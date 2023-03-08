# Generated by Django 4.1.6 on 2023-03-08 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('died', models.BooleanField(default=False)),
                ('firstname', models.CharField(max_length=255)),
            ],
        ),
    ]