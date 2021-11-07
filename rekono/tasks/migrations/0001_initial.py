# Generated by Django 3.2.7 on 2021-11-06 20:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rq_job_id', models.TextField(blank=True, max_length=50, null=True)),
                ('intensity', models.TextField(choices=[('Sneaky', 'Sneaky'), ('Low', 'Low'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Insane', 'Insane')], default='Normal', max_length=10)),
                ('status', models.TextField(choices=[('Requested', 'Requested'), ('Skipped', 'Skipped'), ('Running', 'Running'), ('Cancelled', 'Cancelled'), ('Error', 'Error'), ('Completed', 'Completed')], default='Requested', max_length=10)),
                ('scheduled_at', models.DateTimeField(blank=True, null=True)),
                ('scheduled_in', models.IntegerField(blank=True, null=True)),
                ('scheduled_time_unit', models.TextField(blank=True, choices=[('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks')], max_length=10, null=True)),
                ('repeat_in', models.IntegerField(blank=True, null=True)),
                ('repeat_time_unit', models.TextField(blank=True, choices=[('Minutes', 'Minutes'), ('Hours', 'Hours'), ('Days', 'Days'), ('Weeks', 'Weeks')], max_length=10, null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('configuration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.configuration')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
