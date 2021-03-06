# Generated by Django 3.1.5 on 2021-01-16 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('birthday', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clinika.person')),
                ('sex', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('preliminary_diagnosis', models.CharField(max_length=200, null=True)),
                ('how_the_patient_was_admitted', models.CharField(max_length=400)),
                ('date_of_receipt', models.CharField(max_length=40)),
                ('approximate_growth', models.CharField(max_length=400)),
                ('hair_color', models.CharField(max_length=45)),
                ('identifying_mark', models.CharField(max_length=45)),
                ('statement_date', models.CharField(max_length=45)),
                ('reason_for_discharge', models.CharField(max_length=45)),
                ('Person_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='number1', to='clinika.person')),
            ],
            bases=('clinika.person',),
        ),
        migrations.CreateModel(
            name='Wards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Branch_manager', models.CharField(max_length=60)),
                ('phone_of_ward', models.CharField(max_length=25)),
                ('Patient_ID_of_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinika.patient')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('person_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='clinika.person')),
                ('position', models.CharField(max_length=90)),
                ('Person_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='number2', to='clinika.person')),
            ],
            bases=('clinika.person',),
        ),
        migrations.CreateModel(
            name='Movings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_transfer', models.CharField(max_length=45)),
                ('the_reason_for_the_move', models.CharField(max_length=45)),
                ('Wards_ward_number', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinika.wards')),
                ('Wards_Patient_ID_of_patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinika.patient')),
            ],
        ),
    ]
