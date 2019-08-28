# Generated by Django 2.2.4 on 2019-08-28 06:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vendor', '0001_initial'),
        ('Tracker', '0012_auto_20190823_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracker',
            name='vendor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Vendor.Vendor'),
            preserve_default=False,
        ),
    ]
