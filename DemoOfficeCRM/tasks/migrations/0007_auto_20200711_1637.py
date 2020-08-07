# Generated by Django 3.0.7 on 2020-07-11 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_userdetail_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetail',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userdetail',
            name='designation',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
