from django.contrib import admin
from .models import *

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'manufacture_date', 'expiry_date')
    list_filter = ('manufacture_date', 'expiry_date')
    search_fields = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'price')
        }),
        ('Dates', {
            'fields': ('manufacture_date', 'expiry_date'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'address', 'phone_number')
    list_filter = ('dob',)
    search_fields = ('name', 'address')

    fieldsets = (
        (None, {
            'fields': ('name', 'dob')
        }),
        ('Contact Info', {
            'fields': ('address', 'phone_number'),
            'classes': ('collapse',) 
        }),
    )


@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model_name', 'processor', 'ram_size', 'storage_capacity', 'screen_size', 'price')
    list_filter = ('brand', 'processor')
    search_fields = ('brand', 'model_name')

    fieldsets = (
        (None, {
            'fields': ('brand', 'model_name')
        }),
        ('Specifications', {
            'fields': ('processor', 'ram_size', 'storage_capacity', 'screen_size', 'price'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'age' ,'qualification' , 'gender' , 'salary' ,'exprience')
    list_filter = ('age' ,'salary')
    search_fields = ('age' , 'gender ')

    fieldsets = (
        ( None, {
              'fields': ('exprience', 'salary')
        }),
        ('Specification', {
              'fields': ( 'age','qualifiaction','gender',),
              'classes': ('collapse',)
        }),
    )


