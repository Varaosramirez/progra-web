from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('<int:id>/', views.sale_detail, name='sale_detail'),
    path('create/', views.sale_create, name='sale_create'),
]
