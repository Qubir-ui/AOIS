from django import forms

class AddWard(forms.Form):
    Branch_manager = forms.CharField(label="Заведующий палатой")
    phone_of_ward = forms.CharField(label="Телефон палаты")
    Patient_ID_of_patient = forms.CharField(label="ID пациента")


class AddMovings(forms.Form):
    date_of_transfer = forms.CharField(label="Дата перевода")
    the_reason_for_the_move = forms.CharField(label="Причина перевода")
    Wards_ward_number = forms.CharField(label="Номер палаты")
    Wards_Patient_ID_of_patient = forms.CharField(label="ID пациента")

class AddPatient(forms.Form):
    sex = forms.CharField(label="Пол")
    age = forms.CharField(label="Возраст")
    preliminary_diagnosis = forms.CharField(label="Предварительный диагноз")
    how_the_patient_was_admitted = forms.CharField(label="Как пациент был доставлен")
    date_of_receipt = forms.CharField(label="Дата поступления")
    approximate_growth = forms.CharField(label="Приблизительный рост")
    hair_color = forms.CharField(label="Цвет волос")
    identifying_mark = forms.CharField(label="Особые приметы")
    statement_date = forms.CharField(label="Дата выписки")
    reason_for_discharge = forms.CharField(label="Причина выписки")
    Person_number = forms.CharField(label="ID пациента")

class AddPerson(forms.Form):
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")
    birthday = forms.CharField(label="День рождения")

class AddUser(forms.Form):
    position = forms.CharField(label="Должность")
    Person_number = forms.CharField(label="ID пользователя")






