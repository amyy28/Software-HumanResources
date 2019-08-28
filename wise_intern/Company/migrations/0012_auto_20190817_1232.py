# Generated by Django 2.2.4 on 2019-08-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0011_auto_20190817_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='CTC_type',
            field=models.CharField(choices=[('Fixed', 'Fixed'), ('Gross', 'Gross')], default='Fixed', help_text="Only required if 'shipping' is selected.", max_length=20),
        ),
    ]