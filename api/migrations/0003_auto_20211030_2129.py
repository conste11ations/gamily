# Generated by Django 3.2.8 on 2021-10-30 21:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_profile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileContext',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_score', models.PositiveSmallIntegerField(default=0)),
                ('net_worth', models.IntegerField(default=0)),
                ('assets_mv', models.IntegerField(default=0)),
                ('liabilities_mv', models.IntegerField(default=0)),
                ('insurance', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=10), size=None)),
                ('income', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=2), size=None)),
                ('expenses', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), size=2), size=None)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='experience',
            new_name='age',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='level',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='net_worth',
        ),
        migrations.AddField(
            model_name='answer',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(default='saving', max_length=100),
            preserve_default=False,
        ),
    ]