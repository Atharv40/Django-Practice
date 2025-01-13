from django import forms
from .models import Hospital, Doctor, Patient, Administrative

class HospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = ['name','location','contact_email']

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','specialization','hospitals']

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name','age','ailment','doctor']

class AdministrativeForm(forms.ModelForm):
    class Meta:
        model = Administrative
        fields = ['name','role','hospital']
