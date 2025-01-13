from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Hospital Views
def hospital_list(request):
    hospitals = Hospital.objects.all()
    return render(request, 'hospital_list.html', {'hospitals': hospitals})

def hospital_create(request):
    if request.method == 'POST':
        form = HospitalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm()
    return render(request, 'hospital_form.html', {'form': form})

def hospital_update(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        form = HospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            return redirect('hospital_list')
    else:
        form = HospitalForm(instance=hospital)
    return render(request, 'hospital_form.html', {'form': form})

def hospital_delete(request, pk):
    hospital = get_object_or_404(Hospital, pk=pk)
    if request.method == 'POST':
        hospital.delete()
        return redirect('hospital_list')
    return render(request, 'hospital_confirm_delete.html', {'hospital': hospital})


# Doctor Views
def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

def doctor_create(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm()
    return render(request, 'doctor_form.html', {'form': form})

def doctor_update(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctor_list')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'doctor_form.html', {'form': form})

def doctor_delete(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctor_list')
    return render(request, 'doctor_confirm_delete.html', {'doctor': doctor})


# Patient Views
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def patient_create(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient_form.html', {'form': form})

def patient_update(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient_form.html', {'form': form})

def patient_delete(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('patient_list')
    return render(request, 'patient_confirm_delete.html', {'patient': patient})


# Administrative Views
def administrative_list(request):
    administratives = Administrative.objects.all()
    return render(request, 'administrative_list.html', {'administratives': administratives})

def administrative_create(request):
    if request.method == 'POST':
        form = AdministrativeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administrative_list')
    else:
        form = AdministrativeForm()
    return render(request, 'administrative_form.html', {'form': form})

def administrative_update(request, pk):
    administrative = get_object_or_404(Administrative, pk=pk)
    if request.method == 'POST':
        form = AdministrativeForm(request.POST, instance=administrative)
        if form.is_valid():
            form.save()
            return redirect('administrative_list')
    else:
        form = AdministrativeForm(instance=administrative)
    return render(request, 'administrative_form.html', {'form': form})

def administrative_delete(request, pk):
    administrative = get_object_or_404(Administrative, pk=pk)
    if request.method == 'POST':
        administrative.delete()
        return redirect('administrative_list')
    return render(request, 'administrative_confirm_delete.html', {'administrative': administrative})





