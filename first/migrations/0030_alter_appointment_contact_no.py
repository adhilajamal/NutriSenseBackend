# Generated by Django 5.0.4 on 2024-06-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0029_appointment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='contact_no',
            field=models.BigIntegerField(default=0),
        ),
    ]