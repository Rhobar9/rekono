# Generated by Django 3.2.11 on 2022-01-31 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=50, unique=True)),
                ('description', models.TextField(max_length=250)),
                ('defectdojo_product_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
