# Generated by Django 2.2.4 on 2019-08-16 08:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Job_openings', '0006_auto_20190814_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobb',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.Company'),
        ),
    ]
