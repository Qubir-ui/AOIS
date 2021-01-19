from django.test import TestCase
from clinika.models import Person, Wards, Patient, Movings, User
from django.urls import reverse

class Wards_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Wards.objects.create(id=1, Branch_manager="Курганова Лариса", phone_of_ward="15")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Wards/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Wards'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Wards'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'clinika/Template_Wards.html')

class Person_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Person.objects.create(id=1, first_name="Andrey", last_name="Popov", birthday="20.02.2001")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Person/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Person'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Person'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'clinika/Template_person.html')

class Patient_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Patient.objects.create(sex="мужской", age="19", preliminary_diagnosis="ОРЗ",
                               how_the_patient_was_admitted="Пришел", date_of_receipt="10.01.2021",
                               approximate_growth="170", hair_color="черный", identifying_mark="нет",
                               statement_date="нет", reason_for_discharge="нет")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Patient/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Patient'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Patient'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'clinika/Template_patient.html')

class Movings_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        Movings.objects.create(id=1, date_of_transfer="19.01.2021", the_reason_for_the_move="-")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/Movings/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('Movings'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('Movings'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'clinika/Template_Movings.html')

class User_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create(position="Гл.врач")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/User/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('User'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('User'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'clinika/Template_User.html')

class AnotherViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Wards.objects.create(id=1, Branch_manager="Курганова Лариса", phone_of_ward="15")

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/AOIS/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'index.html')

    def test_view_url_exists_at_desired_location1(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name1(self):
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template1(self):
        resp = self.client.get(reverse('great'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'great.html')