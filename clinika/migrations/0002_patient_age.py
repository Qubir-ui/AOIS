# Generated by Django 3.1.5 on 2021-01-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinika', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]