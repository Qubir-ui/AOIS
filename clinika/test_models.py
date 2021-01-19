from django.test import TestCase
from clinika.models import Person, Wards, Patient, Movings, User


class Wards_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Wards.objects.create(id=1, Branch_manager="Курганова Лариса", phone_of_ward="15")

    def test_id_label(self):
        wards = Wards.objects.get(id=1)
        field_label = wards._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_Branch_manager_label(self):
        wards = Wards.objects.get(id=1)
        field_label = wards._meta.get_field('Branch_manager').verbose_name
        self.assertEquals(field_label,'Branch manager')

    def test_phone_of_ward_label(self):
        wards = Wards.objects.get(id=1)
        field_label = wards._meta.get_field('phone_of_ward').verbose_name
        self.assertEquals(field_label, 'phone of ward')

    def test_Branch_manager_length(self):
        wards = Wards.objects.get(id=1)
        max_length = wards._meta.get_field('Branch_manager').max_length
        self.assertEquals(max_length,60)

    def test_phone_of_ward_max_length(self):
        wards = Wards.objects.get(id=1)
        max_length = wards._meta.get_field('phone_of_ward').max_length
        self.assertEquals(max_length,25)

class Movings_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Movings.objects.create(id=1, date_of_transfer="19.01.2021", the_reason_for_the_move="-")

    def test_id_label(self):
        movings = Movings.objects.get(id=1)
        field_label = movings._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_date_of_transfer_label(self):
        movings = Movings.objects.get(id=1)
        field_label = movings._meta.get_field('date_of_transfer').verbose_name
        self.assertEquals(field_label,'date of transfer')

    def test_the_reason_for_the_move_label(self):
        movings = Movings.objects.get(id=1)
        field_label = movings._meta.get_field('the_reason_for_the_move').verbose_name
        self.assertEquals(field_label, 'the reason for the move')

    def test_date_of_transfer_length(self):
        movings = Movings.objects.get(id=1)
        max_length = movings._meta.get_field('date_of_transfer').max_length
        self.assertEquals(max_length,45)

    def test_the_reason_for_the_move_max_length(self):
        movings = Movings.objects.get(id=1)
        max_length = movings._meta.get_field('the_reason_for_the_move').max_length
        self.assertEquals(max_length,45)

class Person_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Person.objects.create(id=1, first_name="Andrey", last_name="Popov", birthday="20.02.2001")

    def test_id_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('id').verbose_name
        self.assertEquals(field_label,'id')

    def test_first_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('first_name').verbose_name
        self.assertEquals(field_label,'first name')

    def test_last_name_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('last_name').verbose_name
        self.assertEquals(field_label, 'last name')

    def test_birthday_label(self):
        person = Person.objects.get(id=1)
        field_label = person._meta.get_field('birthday').verbose_name
        self.assertEquals(field_label, 'birthday')

    def test_first_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('first_name').max_length
        self.assertEquals(max_length,45)

    def test_last_name_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('last_name').max_length
        self.assertEquals(max_length,45)

    def test_birthday_max_length(self):
        person = Person.objects.get(id=1)
        max_length = person._meta.get_field('birthday').max_length
        self.assertEquals(max_length,45)

class Patient_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Patient.objects.create(sex="мужской", age="19", preliminary_diagnosis="ОРЗ",
                               how_the_patient_was_admitted="Пришел", date_of_receipt="10.01.2021",
                               approximate_growth="170", hair_color="черный", identifying_mark="нет",
                               statement_date="нет", reason_for_discharge="нет")

    def test_sex_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('sex').verbose_name
        self.assertEquals(field_label, 'sex')

    def test_sex_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('sex').max_length
        self.assertEquals(max_length, 40)

    def test_preliminary_diagnosis_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('preliminary_diagnosis').verbose_name
        self.assertEquals(field_label, 'preliminary diagnosis')

    def test_preliminary_diagnosis_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('preliminary_diagnosis').max_length
        self.assertEquals(max_length, 200)

    def test_how_the_patient_was_admitted_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('how_the_patient_was_admitted').verbose_name
        self.assertEquals(field_label, 'how the patient was admitted')

    def test_how_the_patient_was_admitted_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('how_the_patient_was_admitted').max_length
        self.assertEquals(max_length, 400)

    def test_date_of_receipt_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('date_of_receipt').verbose_name
        self.assertEquals(field_label, 'date of receipt')

    def test_date_of_receipt_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('date_of_receipt').max_length
        self.assertEquals(max_length, 40)

    def test_approximate_growth_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('approximate_growth').verbose_name
        self.assertEquals(field_label, 'approximate growth')

    def test_approximate_growth_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('approximate_growth').max_length
        self.assertEquals(max_length, 400)

    def test_hair_color_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('hair_color').verbose_name
        self.assertEquals(field_label, 'hair color')

    def test_hair_color_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('hair_color').max_length
        self.assertEquals(max_length, 45)

    def test_identifying_mark_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('identifying_mark').verbose_name
        self.assertEquals(field_label, 'identifying mark')

    def test_identifying_mark_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('identifying_mark').max_length
        self.assertEquals(max_length, 45)

    def test_statement_date_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('statement_date').verbose_name
        self.assertEquals(field_label, 'statement date')

    def test_statement_date_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('statement_date').max_length
        self.assertEquals(max_length, 45)

    def test_reason_for_discharge_label(self):
        patient = Patient.objects.get(id=1)
        field_label = patient._meta.get_field('reason_for_discharge').verbose_name
        self.assertEquals(field_label, 'reason for discharge')

    def test_reason_for_discharge_max_length(self):
        patient = Patient.objects.get(id=1)
        max_length = patient._meta.get_field('reason_for_discharge').max_length
        self.assertEquals(max_length, 45)

class User_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(position="Гл.врач")

    def test_position_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('position').verbose_name
        self.assertEquals(field_label,'position')

    def test_position_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('position').max_length
        self.assertEquals(max_length,90)
