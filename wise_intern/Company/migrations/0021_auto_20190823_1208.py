# Generated by Django 2.2.4 on 2019-08-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0020_auto_20190823_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='value',
            field=models.CharField(help_text='Enter ₹ for Fixed, % for Percentage', max_length=20),
        ),
    ]