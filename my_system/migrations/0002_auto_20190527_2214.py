# Generated by Django 2.2.1 on 2019-05-27 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train_data',
            name='trainName',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='train_data',
            name='trainNumber',
            field=models.CharField(max_length=5, unique=True),
        ),
    ]
