# Generated by Django 3.1.5 on 2021-01-16 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinika', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='wards',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
