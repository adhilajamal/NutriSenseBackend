# Generated by Django 5.0.4 on 2024-05-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_patient_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient',
            name='contact',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='f', max_length=20),
            preserve_default=False,
        ),
    ]
