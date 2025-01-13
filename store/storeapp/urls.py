from django.urls import path
from .views import *
from .api import *

urlpatterns = [
    # Views for HTML rendering
    path('', store_list_view, name='store-list'),
    path('<int:pk>/', store_detail_view, name='store-detail'),
    path('create/', store_create_view, name='store-create'),
    path('update/<int:pk>/', store_update_view, name='store-update'),
    path('delete/<int:pk>/', store_delete_view, name='store-delete'),

    # API endpoints
    path('api/stores/', StoreListCreateAPIView.as_view(), name='api-store-list-create'),
    path('api/stores/<int:pk>/', StoreDetailAPIView.as_view(), name='api-store-detail'),
]
