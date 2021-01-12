from django.contrib import admin
from .models import Wards, Movings, Patient, Person, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('position','Person_number')

@admin.register(Wards)
class WardsAdmin(admin.ModelAdmin):
    list_display = ('Branch_manager','phone_of_ward','Patient_ID_of_patient')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','birthday')

@admin.register(Movings)
class MovingsAdmin(admin.ModelAdmin):
    list_display = ('date_of_transfer','the_reason_for_the_move','Wards_ward_number','Wards_Patient_ID_of_patient')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('sex','age','preliminary_diagnosis','how_the_patient_was_admitted','date_of_receipt',
                    'approximate_growth','hair_color','identifying_mark','statement_date','reason_for_discharge',
                    'Person_number')

