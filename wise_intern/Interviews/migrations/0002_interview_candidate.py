# Generated by Django 2.2.4 on 2019-08-12 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Candidate', '0001_initial'),
        ('Interviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='interview',
            name='candidate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Candidate.Candidate'),
            preserve_default=False,
        ),
    ]