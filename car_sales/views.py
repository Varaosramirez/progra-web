from django.shortcuts import render
from vehicles.models import Vehicle
from employees.models import Employee

def home(request):
    context = {}
    if request.user.is_authenticated and request.user.is_admin:
        vehicles = Vehicle.objects.all()
        employees = Employee.objects.all()
        context = {
            'vehicles': vehicles,
            'employees': employees
        }
    return render(request, 'home.html', context)
