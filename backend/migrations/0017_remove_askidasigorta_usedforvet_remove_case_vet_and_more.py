# Generated by Django 4.0 on 2021-12-26 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='askidasigorta',
            name='usedForVet',
        ),
        migrations.RemoveField(
            model_name='case',
            name='vet',
        ),
        migrations.RemoveField(
            model_name='claim',
            name='veterinary',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='vet',
        ),
        migrations.AddField(
            model_name='vet',
            name='address',
            field=models.CharField(default='test', max_length=100),
        ),
        migrations.AddField(
            model_name='vet',
            name='phone',
            field=models.CharField(default='05398376436', max_length=100),
        ),
    ]
