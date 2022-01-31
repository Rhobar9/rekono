# Generated by Django 3.2.11 on 2022-01-31 07:20

from django.db import migrations, models
import input_types.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wordlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, unique=True)),
                ('type', models.TextField(choices=[('Password', 'Password'), ('Endpoint', 'Endpoint')], max_length=10)),
                ('path', models.TextField(max_length=200, unique=True)),
                ('checksum', models.TextField(blank=True, max_length=128, null=True)),
                ('size', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
            bases=(models.Model, input_types.base.BaseInput),
        ),
    ]
