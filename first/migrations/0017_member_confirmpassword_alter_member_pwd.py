# Generated by Django 5.0.4 on 2024-05-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0016_remove_member_confirmpassword_alter_member_pwd'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='confirmpassword',
            field=models.CharField(default=123, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='pwd',
            field=models.CharField(max_length=20),
        ),
    ]