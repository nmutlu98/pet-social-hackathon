# Generated by Django 4.0 on 2021-12-26 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_pet_chronicalillnesses'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('rate', models.IntegerField(verbose_name=0)),
                ('big_image', models.CharField(max_length=200)),
                ('background', models.CharField(max_length=200)),
                ('date', models.DateField(verbose_name='date')),
            ],
        ),
        migrations.CreateModel(
            name='Walker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(max_length=200)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('rate', models.IntegerField(verbose_name=0)),
                ('big_image', models.CharField(max_length=200)),
                ('background', models.CharField(max_length=200)),
                ('date', models.DateField(verbose_name='date')),
            ],
        ),
    ]
