# Generated by Django 5.0.4 on 2024-05-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0013_rename_role_member_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='role',
            field=models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor')], default='patient', max_length=20),
            preserve_default=False,
        ),
    ]
