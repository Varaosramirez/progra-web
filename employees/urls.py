from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('<int:id>/', views.employee_detail, name='employee_detail'),
    path('create/', views.employee_create, name='employee_create'),
    path('add/', views.add_employee, name='add_employee'),
    path('edit/<int:id>/', views.edit_employee, name='edit_employee'),  # URL para editar
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),  # URL para eliminar

]
