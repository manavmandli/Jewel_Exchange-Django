# Generated by Django 4.2.2 on 2023-06-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonialsmodel',
            name='organization_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testimonialsmodel',
            name='position',
            field=models.CharField(choices=[('Owner', 'Owner'), ('Employee', 'Employee'), ('Manager', 'Manager')], default='Owner', max_length=50),
        ),
    ]