# Generated by Django 5.1.6 on 2025-03-03 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myapp',
            name='joined_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='myapp',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
