# Generated by Django 2.2.4 on 2019-08-19 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0012_auto_20190819_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='experience_months',
        ),
        migrations.RemoveField(
            model_name='candidate',
            name='experience_years',
        ),
        migrations.AddField(
            model_name='candidate',
            name='experience',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='candidate',
            name='new_experience',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
