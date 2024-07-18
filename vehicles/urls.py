from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('<int:id>/', views.vehicle_detail, name='vehicle_detail'),
    path('create/', views.vehicle_create, name='vehicle_create'),
    path('add/', views.add_vehicle, name='add_vehicle'),
    path('delete/<int:id>/', views.delete_vehicle, name='delete_vehicle'),  # URL para eliminar
    path('edit/<int:id>/', views.edit_vehicle, name='edit_vehicle'),  # URL para editar



]
