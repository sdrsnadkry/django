# Generated by Django 3.0.7 on 2020-06-21 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0015_auto_20200621_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='package_image',
            field=models.ImageField(default='', upload_to='BackendImages/Packages'),
        ),
    ]
