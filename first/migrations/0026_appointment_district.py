# Generated by Django 5.0.4 on 2024-05-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0025_appointment_patient_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='district',
            field=models.CharField(default=set, max_length=20),
            preserve_default=False,
        ),
    ]
