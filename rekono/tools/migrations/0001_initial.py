# Generated by Django 3.2.7 on 2021-10-11 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('arguments', models.TextField(blank=True, default='', max_length=250)),
                ('default', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30, unique=True)),
                ('command', models.TextField(blank=True, max_length=30, null=True)),
                ('stage', models.IntegerField(choices=[(1, 'Osint'), (2, 'Enumeration'), (3, 'Vulnerabilities'), (4, 'Services'), (5, 'Exploitation')])),
                ('reference', models.TextField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Osint'), (2, 'Host'), (3, 'Enumeration'), (4, 'Url'), (5, 'Http Endpoint'), (6, 'Technology'), (7, 'Vulnerability'), (8, 'Exploit'), (9, 'Parameter')])),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='tools.configuration')),
            ],
        ),
        migrations.CreateModel(
            name='Intensity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argument', models.TextField(blank=True, default='', max_length=50)),
                ('value', models.IntegerField(choices=[(1, 'Sneaky'), (2, 'Low'), (3, 'Normal'), (4, 'Hard'), (5, 'Insane')], default=3)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intensities', to='tools.tool')),
            ],
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('type', models.IntegerField(choices=[(1, 'Osint'), (2, 'Host'), (3, 'Enumeration'), (4, 'Url'), (5, 'Http Endpoint'), (6, 'Technology'), (7, 'Vulnerability'), (8, 'Exploit'), (9, 'Parameter')])),
                ('argument', models.TextField(blank=True, default='', max_length=50)),
                ('filter', models.TextField(blank=True, max_length=250, null=True)),
                ('selection', models.IntegerField(choices=[(1, 'All'), (2, 'For Each')], default=2)),
                ('required', models.BooleanField(default=False)),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='tools.configuration')),
            ],
        ),
        migrations.AddField(
            model_name='configuration',
            name='tool',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='tools.tool'),
        ),
        migrations.AddConstraint(
            model_name='output',
            constraint=models.UniqueConstraint(fields=('configuration', 'type'), name='unique output'),
        ),
        migrations.AddConstraint(
            model_name='input',
            constraint=models.UniqueConstraint(fields=('configuration', 'name'), name='unique input'),
        ),
        migrations.AddConstraint(
            model_name='configuration',
            constraint=models.UniqueConstraint(fields=('tool', 'name'), name='unique configuration'),
        ),
    ]
