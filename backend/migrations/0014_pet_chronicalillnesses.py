# Generated by Django 4.0 on 2021-12-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_case_vet'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='chronicalIllnesses',
            field=models.CharField(default='diabet', max_length=100),
        ),
    ]
