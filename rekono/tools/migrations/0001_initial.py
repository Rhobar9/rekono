# Generated by Django 3.2.7 on 2021-11-06 20:15

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
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30, unique=True)),
                ('command', models.TextField(blank=True, max_length=30, null=True)),
                ('output_format', models.TextField(blank=True, max_length=5, null=True)),
                ('defectdojo_scan_type', models.TextField(blank=True, max_length=50, null=True)),
                ('stage', models.TextField(choices=[('OSINT', 'Osint'), ('Enumeration', 'Enumeration'), ('Vulnerabilities analysis', 'Vulnerabilities'), ('Services analysis', 'Services'), ('Exploitation', 'Exploitation')], max_length=25)),
                ('reference', models.TextField(blank=True, max_length=250, null=True)),
                ('icon', models.TextField(blank=True, max_length=250, null=True)),
                ('for_each_target_port', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(choices=[('OSINT', 'Osint'), ('Host', 'Host'), ('Enumeration', 'Enumeration'), ('Endpoint', 'Endpoint'), ('Technology', 'Technology'), ('Vulnerability', 'Vulnerability'), ('Exploit', 'Exploit'), ('Credential', 'Credential'), ('Wordlist', 'Wordlist')], max_length=15)),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='outputs', to='tools.configuration')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Intensity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('argument', models.TextField(blank=True, default='', max_length=50)),
                ('value', models.TextField(choices=[('Sneaky', 'Sneaky'), ('Low', 'Low'), ('Normal', 'Normal'), ('Hard', 'Hard'), ('Insane', 'Insane')], default='Normal', max_length=10)),
                ('tool', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intensities', to='tools.tool')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Input',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('type', models.TextField(choices=[('OSINT', 'Osint'), ('Host', 'Host'), ('Enumeration', 'Enumeration'), ('Endpoint', 'Endpoint'), ('Technology', 'Technology'), ('Vulnerability', 'Vulnerability'), ('Exploit', 'Exploit'), ('Credential', 'Credential'), ('Wordlist', 'Wordlist')], max_length=15)),
                ('argument', models.TextField(blank=True, default='', max_length=50)),
                ('filter', models.TextField(blank=True, max_length=250, null=True)),
                ('selection', models.TextField(choices=[('All', 'All'), ('For Each', 'For Each')], default='For Each', max_length=10)),
                ('required', models.BooleanField(default=False)),
                ('configuration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputs', to='tools.configuration')),
            ],
            options={
                'ordering': ['-id'],
            },
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
            constraint=models.UniqueConstraint(fields=('configuration', 'type'), name='unique input'),
        ),
        migrations.AddConstraint(
            model_name='configuration',
            constraint=models.UniqueConstraint(fields=('tool', 'name'), name='unique configuration'),
        ),
    ]
