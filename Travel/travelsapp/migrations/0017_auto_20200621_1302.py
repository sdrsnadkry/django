# Generated by Django 3.0.7 on 2020-06-21 07:17

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0016_auto_20200621_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packages',
            name='package_image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, size=[500, 500], upload_to='BackendImages/Packages'),
        ),
    ]
