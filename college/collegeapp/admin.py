from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
   
    list_display = ('name', 'location',  'contact_email','total_student')

    search_fields = ('name', 'location')

    list_filter = ( 'total_student','location')
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location')
        }),
        ('Additional Details', {
            'fields': ( 'total_student','contact_email'),
            'classes': ('collapse',), 
        }),
    )

