# Generated by Django 3.2.16 on 2022-12-18 13:15

from django.db import migrations, models
import django.db.models.deletion
import input_types.base
import security.input_validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('targets', '0003_auto_20221218_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputVulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cve', models.TextField(max_length=20, validators=[security.input_validation.validate_cve])),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_vulnerabilities', to='targets.target')),
            ],
            bases=(models.Model, input_types.base.BaseInput),
        ),
        migrations.CreateModel(
            name='InputTechnology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100, validators=[security.input_validation.validate_name])),
                ('version', models.TextField(blank=True, max_length=100, null=True, validators=[security.input_validation.validate_name])),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='input_technologies', to='targets.target')),
            ],
            bases=(models.Model, input_types.base.BaseInput),
        ),
        migrations.AddConstraint(
            model_name='inputvulnerability',
            constraint=models.UniqueConstraint(fields=('target', 'cve'), name='unique input vulnerability'),
        ),
        migrations.AddConstraint(
            model_name='inputtechnology',
            constraint=models.UniqueConstraint(fields=('target', 'name', 'version'), name='unique input technology'),
        ),
    ]
