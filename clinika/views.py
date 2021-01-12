from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template.context_processors import csrf
from django.views.generic import FormView
from .models import Wards, Movings, Patient, Person, User
from .forms import AddWard, AddMovings, AddPatient, AddPerson, AddUser
from django.views import generic
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import FormView
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.http import HttpResponseNotFound

from clinika import forms

def great(request):
    return render(request, "great.html")

def index(request):
    return render(request, "index.html")

def index_wards(request): #index_author
    form_add = AddWard()
    data = Wards.objects.all()
    return render(request, "clinika/Template_Wards.html", {"form":form_add, "data_show":data})

def index_Movings(request): #index_exhibition
    form_ex = AddMovings()
    data = Movings.objects.all()
    return render(request, "clinika/Template_Movings.html", {"form":form_ex, "data_show":data})

def index_patient(request):
    form_er = AddPatient
    data = Patient.objects.all()
    return render(request, "clinika/Template_patient.html", {"form":form_er, "data_show":data})

def index_user(request):
    form_ca = AddUser
    data = User.objects.all()
    return render(request, "clinika/Template_User.html", {"form":form_ca, "data_show":data})

def index_person(request):
    form_ra = AddPerson
    data = Person.objects.all()
    return render(request, "clinika/Template_person.html", {"form":form_ra, "data_show":data})

#Определение view

class view_patient(View):
    def add_patient(request):
        if request.method == "POST":
            patient = Patient()
            patient.sex = request.POST.get("sex")
            patient.age = request.POST.get("age")
            patient.preliminary_diagnosis = request.POST.get("preliminary_diagnosis")
            patient.how_the_patient_was_admitted = request.POST.get("how_the_patient_was_admitted")
            patient.date_of_receipt = request.POST.get("date_of_receipt")
            patient.approximate_growth = request.POST.get("approximate_growth")
            patient.hair_color = request.POST.get("hair_color")
            patient.identifying_mark = request.POST.get("identifying_mark")
            patient.statement_date = request.POST.get("statement_date")
            patient.reason_for_discharge = request.POST.get("reason_for_discharge")
            patient.Person_number = Person.objects.get(id=request.POST.get("Person_number"))
            patient.save()
            return HttpResponseRedirect("/Patient")

    def del_patient(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Patient.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Patient")

    def update_patient(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Patient.objects.get(id=q)
            que.sex = request.POST.get("sex")
            que.age = request.POST.get("age")
            que.preliminary_diagnosis = request.POST.get("preliminary_diagnosis")
            que.how_the_patient_was_admitted = request.POST.get("how_the_patient_was_admitted")
            que.date_of_receipt = request.POST.get("date_of_receipt")
            que.approximate_growth = request.POST.get("approximate_growth")
            que.hair_color = request.POST.get("hair_color")
            que.identifying_mark = request.POST.get("identifying_mark")
            que.statement_date = request.POST.get("statement_date")
            que.reason_for_discharge = request.POST.get("reason_for_discharge")
            que.Person_number = Person.objects.get(id=request.POST.get("Person_number"))
            que.save()
            return HttpResponseRedirect("/Patient")

class view_user(View):
    def add_user(request):
        if request.method == "POST":
            user = User()
            user.position = request.POST.get("position")
            user.Person_number = Person.objects.get(id=request.POST.get("Person_number"))
            user.save()
            return HttpResponseRedirect("/User")

    def del_user(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = User.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/User")

    def update_user(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = User.objects.get(id=q)
            que.position = request.POST.get("position")
            que.Person_number = Person.objects.get(id=request.POST.get("Person_number"))
            que.save()
            return HttpResponseRedirect("/User")

class view_Movings(View):
    def add_Movings(request):
        if request.method == "POST":
            movings = Movings()
            movings.date_of_transfer = request.POST.get("date_of_transfer")
            movings.the_reason_for_the_move = request.POST.get("the_reason_for_the_move")
            movings.Wards_ward_number = Wards.objects.get(id=request.POST.get("Wards_ward_number"))
            movings.Wards_Patient_ID_of_patient = Patient.objects.get(id=request.POST.get("Wards_Patient_ID_of_patient"))
            movings.save()
            return HttpResponseRedirect("/Movings")

    def del_Movings(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Movings.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Movings")

    def update_Movings(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Movings.objects.get(id=q)
            que.date_of_transfer = request.POST.get("date_of_transfer")
            que.the_reason_for_the_move = request.POST.get("the_reason_for_the_move")
            que.Wards_ward_number = Wards.objects.get(id=request.POST.get("Wards_ward_number"))
            que.Wards_Patient_ID_of_patient = Patient.objects.get(id=request.POST.get("Wards_Patient_ID_of_patient"))
            que.save()
            return HttpResponseRedirect("/Movings")

class view_ward(View):
    def add_ward(request):
        if request.method == "POST":
            ward = Wards()
            ward.Branch_manager = request.POST.get("Branch_manager")
            ward.phone_of_ward = request.POST.get("phone_of_ward")
            ward.Patient_ID_of_patient = Patient.objects.get(id=request.POST.get("Patient_ID_of_patient"))
            ward.save()
            return HttpResponseRedirect("/Wards")

    def del_ward(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Wards.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Wards")

    def update_ward(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Wards.objects.get(id=q)
            que.Branch_manager = request.POST.get("Branch_manager")
            que.phone_of_ward = request.POST.get("phone_of_ward")
            que.Patient_ID_of_patient = Patient.objects.get(id=request.POST.get("Patient_ID_of_patient"))
            que.save()
            return HttpResponseRedirect("/Wards")

class view_Person(View):
    def add_Person(request):
        if request.method == "POST":
            person = Person()
            person.first_name = request.POST.get("first_name")
            person.last_name = request.POST.get("last_name")
            person.birthday = request.POST.get("birthday")
            person.save()
            return HttpResponseRedirect("/Person")

    def del_Person(request):
        if request.method == "POST":
            q = request.POST.get("delname", "")
            que = Person.objects.get(id=q)
            que.delete()
            return HttpResponseRedirect("/Person")

    def update_Person(request):
        if request.method == "POST":
            q = request.POST.get("upname", "")
            que = Person.objects.get(id=q)
            que.first_name = request.POST.get("first_name")
            que.last_name = request.POST.get("last_name")
            que.birthday = request.POST.get("birthday")
            que.save()
            return HttpResponseRedirect("/Person")



