# Generated by Django 3.2.7 on 2021-10-11 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Execution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rq_job_id', models.TextField(blank=True, max_length=50, null=True)),
                ('rq_job_pid', models.IntegerField(blank=True, null=True)),
                ('output_file', models.TextField(blank=True, max_length=50, null=True)),
                ('output_plain', models.TextField(blank=True, null=True)),
                ('output_error', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(choices=[(1, 'Requested'), (2, 'Skipped'), (3, 'Running'), (4, 'Cancelled'), (5, 'Error'), (6, 'Completed')], default=1)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.IntegerField(choices=[(1, 'Technology'), (2, 'Version'), (3, 'Http Endpoint'), (4, 'Cve'), (5, 'Exploit'), (6, 'Wordlist')])),
                ('value', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rq_job_id', models.TextField(blank=True, max_length=50, null=True)),
                ('intensity', models.IntegerField(choices=[(1, 'Sneaky'), (2, 'Low'), (3, 'Normal'), (4, 'Hard'), (5, 'Insane')], default=3)),
                ('status', models.IntegerField(choices=[(1, 'Requested'), (2, 'Skipped'), (3, 'Running'), (4, 'Cancelled'), (5, 'Error'), (6, 'Completed')], default=1)),
                ('scheduled_at', models.DateTimeField(blank=True, null=True)),
                ('scheduled_in', models.IntegerField(blank=True, null=True)),
                ('scheduled_time_unit', models.IntegerField(blank=True, choices=[(1, 'Minutes'), (2, 'Hours'), (3, 'Days'), (4, 'Weeks')], null=True)),
                ('repeat_in', models.IntegerField(blank=True, null=True)),
                ('repeat_time_unit', models.IntegerField(blank=True, choices=[(1, 'Minutes'), (2, 'Hours'), (3, 'Days'), (4, 'Weeks')], null=True)),
                ('start', models.DateTimeField(blank=True, null=True)),
                ('end', models.DateTimeField(blank=True, null=True)),
                ('configuration', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tools.configuration')),
            ],
        ),
    ]
