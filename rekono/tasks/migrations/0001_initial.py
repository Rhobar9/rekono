# Generated by Django 3.2.7 on 2021-11-06 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0001_initial'),
        ('targets', '0001_initial'),
        ('tools', '0001_initial'),
        ('processes', '0002_initial'),
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
                ('executor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('process', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='processes.process')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='targets.target')),
                ('tool', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.tool')),
                ('wordlists', models.ManyToManyField(blank=True, related_name='wordlists', to='resources.Wordlist')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.TextField(choices=[('Technology', 'Technology'), ('Version', 'Version'), ('Endpoint', 'Endpoint'), ('CVE', 'Cve'), ('Exploit', 'Exploit'), ('Wordlist', 'Wordlist')], max_length=10)),
                ('value', models.TextField(max_length=250)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='tasks.task')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
