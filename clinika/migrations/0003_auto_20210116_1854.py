# Generated by Django 3.1.5 on 2021-01-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinika', '0002_auto_20210116_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movings',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]