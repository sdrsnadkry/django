# Generated by Django 3.0.7 on 2020-07-16 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_auto_20200715_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='TasksStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('remarks', models.TextField(blank=True)),
                ('reassign', models.BooleanField(default=False)),
                ('reassign_description', models.TextField(blank=True)),
                ('reassign_startdate', models.DateTimeField(blank=True)),
                ('reassign_enddate', models.DateTimeField(blank=True)),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tasks.Task')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
