# Generated by Django 2.2.4 on 2019-08-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_openings', '0005_auto_20190814_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobb',
            name='company',
            field=models.CharField(max_length=100),
        ),
    ]
