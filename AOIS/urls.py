
from django.contrib import admin
from django.urls import path
from clinika import views
from django.views.generic import TemplateView
from django.conf.urls import include, url

admin.autodiscover()



urlpatterns = [
    path('',views.great, name='great'),
    url(r'^admin/backups/', include('dbbackup_ui.urls')),
    url(r'^admin/', admin.site.urls),
    path('AOIS/', views.index, name='home'),
    path('Wards/', views.index_wards, name='Wards'),
    path('Movings/', views.index_Movings, name='Movings'),
    path('User/', views.index_user, name='User'),
    path('Patient/', views.index_patient, name='Patient'),
    path('Person/', views.index_person, name='Person'),
    #пути для палат
    path('Wards/add/', views.view_ward.add_ward, name='add_ward'),
    path("Wards/del/", views.view_ward.del_ward, name="del_ward"),
    path("Wards/up/", views.view_ward.update_ward, name="update_ward"),
    #пути для перемещений
    path('Movings/adde/', views.view_Movings.add_Movings, name='add_Movings'),
    path("Movings/dele/", views.view_Movings.del_Movings, name="del_Movings"),
    path("Movings/upe/", views.view_Movings.update_Movings, name="update_Movings"),
    #пути для пользователей
    path('User/addc/', views.view_user.add_user, name='add_user'),
    path("User/delc/", views.view_user.del_user, name="del_user"),
    path("User/upc/", views.view_user.update_user, name="update_user"),
    #пути для пациентов
    path('Patient/addo/', views.view_patient.add_patient, name='add_Patient'),
    path("Patient/delo/", views.view_patient.del_patient, name="del_patient"),
    path("Patient/upo/", views.view_patient.update_patient, name="update_patient"),
    #пути для субъектов
    path('Person/addr/', views.view_Person.add_Person, name='add_Person'),
    path("Person/delr/", views.view_Person.del_Person, name="del_Person"),
    path("Person/upr/", views.view_Person.update_Person, name="update_Person"),
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]