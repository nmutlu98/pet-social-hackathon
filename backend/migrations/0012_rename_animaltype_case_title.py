# Generated by Django 4.0 on 2021-12-25 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0011_askidasigorta'),
    ]

    operations = [
        migrations.RenameField(
            model_name='case',
            old_name='animalType',
            new_name='title',
        ),
    ]
