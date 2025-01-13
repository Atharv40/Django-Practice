from django.urls import path
from . import views

urlpatterns = [
    # Hospital URLs
    path('hospitals/', views.hospital_list, name='hospital_list'),
    path('hospitals/new/', views.hospital_create, name='hospital_create'),
    path('hospitals/<int:pk>/edit/', views.hospital_update, name='hospital_update'),
    path('hospitals/<int:pk>/delete/', views.hospital_delete, name='hospital_delete'),

    # Doctor URLs
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('doctors/new/', views.doctor_create, name='doctor_create'),
    path('doctors/<int:pk>/edit/', views.doctor_update, name='doctor_update'),
    path('doctors/<int:pk>/delete/', views.doctor_delete, name='doctor_delete'),

    # Patient URLs
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/new/', views.patient_create, name='patient_create'),
    path('patients/<int:pk>/edit/', views.patient_update, name='patient_update'),
    path('patients/<int:pk>/delete/', views.patient_delete, name='patient_delete'),

    # Administrative URLs
    path('administratives/', views.administrative_list, name='administrative_list'),
    path('administratives/new/', views.administrative_create, name='administrative_create'),
    path('administratives/<int:pk>/edit/', views.administrative_update, name='administrative_update'),
    path('administratives/<int:pk>/delete/', views.administrative_delete, name='administrative_delete'),
]
