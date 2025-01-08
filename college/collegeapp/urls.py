from django.urls import path
from . import views

urlpatterns = [
    path('app', views.college_list, name='college_list'),           # Read
    path('create/', views.college_create, name='college_create'),  # Create
    path('update/<int:id>/', views.college_update, name='college_update'),  # Update
    path('delete/<int:id>/', views.college_delete, name='college_delete'),  # Delete
]
