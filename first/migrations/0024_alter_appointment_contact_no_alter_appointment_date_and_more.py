# Generated by Django 5.0.4 on 2024-05-25 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0023_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='contact_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.DateField(default='null'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='time',
            field=models.TimeField(default='null'),
        ),
    ]
