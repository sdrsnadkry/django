# Generated by Django 3.0.7 on 2020-06-22 08:35

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0024_auto_20200621_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('title', models.CharField(default='', max_length=500)),
                ('author', models.CharField(default='', max_length=500)),
                ('Date', models.DateField()),
                ('content', models.TextField(default='')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format=None, keep_meta=True, quality=100, size=[1920, 1080], upload_to='BackendImages/Blogs')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
