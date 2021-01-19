from django.test import TestCase
from clinika.forms import AddWard, AddMovings, AddPerson, AddPatient, AddUser

class AddWard_test(TestCase):

    def test_id_label(self):
        form = AddWard()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'Номер палаты')

    def test_Branch_manager_label(self):
        form = AddWard()
        self.assertTrue(form.fields['Branch_manager'].label == None or form.fields['Branch_manager'].label == 'Заведующий палатой')

    def test_phone_of_ward_label(self):
        form = AddWard()
        self.assertTrue(form.fields['phone_of_ward'].label == None or form.fields['phone_of_ward'].label == 'Телефон палаты')

    def test_Patient_ID_of_patient_label(self):
        form = AddWard()
        self.assertTrue(form.fields['Patient_ID_of_patient'].label == None or form.fields['Patient_ID_of_patient'].label == 'ID пациента')

    def test_proverka(self):
        form = AddWard(data={'id': 1, 'Branch_manager': "Ольга Петровна", 'phone_of_ward' : 15, "Patient_ID_of_patient" : 1})
        self.assertTrue(form.is_valid())

class AddMovings_test(TestCase):

    def test_id_label(self):
        form = AddMovings()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'Номер перевода')

    def test_date_of_transfer_label(self):
        form = AddMovings()
        self.assertTrue(form.fields['date_of_transfer'].label == None or form.fields['date_of_transfer'].label == 'Дата перевода')

    def test_the_reason_for_the_move_label(self):
        form = AddMovings()
        self.assertTrue(form.fields['the_reason_for_the_move'].label == None or form.fields['the_reason_for_the_move'].label == 'Причина перевода')

    def test_Wards_ward_number_label(self):
        form = AddMovings()
        self.assertTrue(form.fields['Wards_ward_number'].label == None or form.fields['Wards_ward_number'].label == 'Номер палаты')

    def test_Wards_Patient_ID_of_patient_label(self):
        form = AddMovings()
        self.assertTrue(form.fields['Wards_Patient_ID_of_patient'].label == None or form.fields['Wards_Patient_ID_of_patient'].label == 'ID пациента')

    def test_proverka(self):
        form = AddMovings(data={'id': 1, 'date_of_transfer': "10.01.2021", 'the_reason_for_the_move' : "нет", "Wards_ward_number" : 1, 'Wards_Patient_ID_of_patient' : 1})
        self.assertTrue(form.is_valid())

class AddPerson_test(TestCase):

    def test_id_label(self):
        form = AddPerson()
        self.assertTrue(form.fields['id'].label == None or form.fields['id'].label == 'ID')

    def test_first_name_label(self):
        form = AddPerson()
        self.assertTrue(form.fields['first_name'].label == None or form.fields['first_name'].label == 'Имя')

    def test_last_name_label(self):
        form = AddPerson()
        self.assertTrue(form.fields['last_name'].label == None or form.fields['last_name'].label == 'Фамилия')

    def test_birthday_label(self):
        form = AddPerson()
        self.assertTrue(form.fields['birthday'].label == None or form.fields['birthday'].label == 'День рождения')

    def test_proverka(self):
        form = AddPerson(data={'id': 1, 'first_name': "Andrey", 'last_name' : "Popov", "birthday" : "20.02.2001"})
        self.assertTrue(form.is_valid())

class AddPatient_test(TestCase):

    def test_sex_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['sex'].label == None or form.fields['sex'].label == 'Пол')

    def test_age_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['age'].label == None or form.fields['age'].label == 'Возраст')

    def test_preliminary_diagnosis_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['preliminary_diagnosis'].label == None or form.fields['preliminary_diagnosis'].label == 'Предварительный диагноз')

    def test_how_the_patient_was_admitted_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['how_the_patient_was_admitted'].label == None or form.fields['how_the_patient_was_admitted'].label == 'Как пациент был доставлен')

    def test_date_of_receipt_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['date_of_receipt'].label == None or form.fields['date_of_receipt'].label == 'Дата поступления')

    def test_approximate_growth_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['approximate_growth'].label == None or form.fields['approximate_growth'].label == 'Приблизительный рост')

    def test_hair_color_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['hair_color'].label == None or form.fields['hair_color'].label == 'Цвет волос')

    def test_identifying_mark_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['identifying_mark'].label == None or form.fields['identifying_mark'].label == 'Особые приметы')

    def test_statement_date_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['statement_date'].label == None or form.fields['statement_date'].label == 'Дата выписки')

    def test_reason_for_discharge_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['reason_for_discharge'].label == None or form.fields['reason_for_discharge'].label == 'Причина выписки')

    def test_Person_number_label(self):
        form = AddPatient()
        self.assertTrue(form.fields['Person_number'].label == None or form.fields['Person_number'].label == 'ID пациента')

    def test_proverka(self):
        form = AddPatient(data={"id" : 1,'first_name': "Andrey", 'last_name' : "Popov", "birthday" : "20.02.2001",
                                "sex": "Мужской",
                                "age" : "19",
                                "preliminary_diagnosis" : "ОРЗ",
                                "how_the_patient_was_admitted" : "Направление поликлиники",
                                "date_of_receipt" : "Нет",
                                "approximate_growth" : "170",
                                "hair_color" : "Черный",
                                "identifying_mark" : "Нет",
                                "statement_date" : "Нет",
                                "reason_for_discharge" : "Нет",
                                "Person_number" : "1"})
        self.assertTrue(form.is_valid())

class AddUser_test(TestCase):

    def test_position_label(self):
        form = AddUser()
        self.assertTrue(form.fields['position'].label == None or form.fields['position'].label == 'Должность')

    def test_Person_number_label(self):
        form = AddUser()
        self.assertTrue(form.fields['Person_number'].label == None or form.fields['Person_number'].label == 'ID пользователя')

    def test_proverka(self):
        form = AddUser(data={'id': 1, 'first_name': "Andrey", 'last_name' : "Popov", "birthday" : "20.02.2001",
                               "position" : "Гл.врач", "Person_number" : "1"})
        self.assertTrue(form.is_valid())
