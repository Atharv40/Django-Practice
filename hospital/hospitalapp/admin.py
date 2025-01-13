from django.contrib import admin
from .models import *

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'contact_email')
    search_fields = ('name', 'location')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization')
    search_fields = ('name', 'specialization')
    filter_horizontal = ('hospitals',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'ailment', 'doctor')
    search_fields = ('name', 'ailment')
    list_filter = ('doctor',)

@admin.register(Administrative)
class AdministrativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'hospital')
    search_fields = ('name', 'role')
    list_filter = ('hospital',)
