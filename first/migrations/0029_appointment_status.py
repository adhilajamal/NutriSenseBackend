# Generated by Django 5.0.4 on 2024-06-02 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0028_delete_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=10),
        ),
    ]
