from django.db import models


class Wards(models.Model):
    id = models.IntegerField(primary_key=True)
    Branch_manager = models.CharField(max_length=60)
    phone_of_ward = models.CharField(max_length=25)
    Patient_ID_of_patient = models.ForeignKey('Patient', on_delete=models.CASCADE,
                                              null=True)
    objects = models.Manager()


class Movings(models.Model):
    id = models.IntegerField(primary_key=True)
    date_of_transfer = models.CharField(max_length=45)
    the_reason_for_the_move = models.CharField(max_length=45)
    Wards_ward_number = models.ForeignKey('Wards', on_delete=models.CASCADE,null=True)
    Wards_Patient_ID_of_patient = models.ForeignKey('Patient', on_delete=models.CASCADE
                                                    ,null=True)
    objects = models.Manager()


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birthday = models.CharField(max_length=45)
    objects = models.Manager()


class Patient(Person):
    sex = models.CharField(max_length=40)
    age = models.IntegerField()
    preliminary_diagnosis = models.CharField(max_length=200, null=True)
    how_the_patient_was_admitted = models.CharField(max_length=400)
    date_of_receipt = models.CharField(max_length=40)
    approximate_growth = models.CharField(max_length=400)
    hair_color = models.CharField(max_length=45)
    identifying_mark = models.CharField(max_length=45)
    statement_date = models.CharField(max_length=45)
    reason_for_discharge = models.CharField(max_length=45)
    Person_number = models.ForeignKey('Person', on_delete=models.CASCADE,related_name='number1',null=True)
    objects = models.Manager()


class User(Person):
    position = models.CharField(max_length=90)
    Person_number = models.ForeignKey('Person', on_delete=models.CASCADE,related_name='number2',null=True)
    objects = models.Manager()
