# Generated by Django 5.0.4 on 2024-05-17 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_rename_confirmpasswod_member_confirmpassword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
    ]
