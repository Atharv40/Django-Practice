from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import College
from .forms import CollegeForm

# Read: Display list of colleges
def college_list(request):
    colleges = College.objects.all()
    return render(request, 'college_list.html', {'colleges': colleges})
   # D:\Django Batch\Django-Practice\college\collegeapp\templates\college_list.html

# Create: Add a new college
def college_create(request):
    if request.method == "POST":
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('college_list')
    else:
        form = CollegeForm()
    return render(request, 'college_form.html', {'form': form})

# Update: Edit an existing college
def college_update(request, id):
    college = get_object_or_404(College, id=id)
    if request.method == "POST":
        form = CollegeForm(request.POST, instance=college)
        if form.is_valid():
            form.save()
            return redirect('college_list')
    else:
        form = CollegeForm(instance=college)
    return render(request, 'college_form.html', {'form': form})

# Delete: Remove a college
def college_delete(request, id):
    college = get_object_or_404(College, id=id)
    if request.method == "POST":
        college.delete()
        return redirect('college_list')
    return render(request, 'college_confirm_delete.html', {'college': college})
