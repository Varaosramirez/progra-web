from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Employee
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required
from .forms import EmployeeForm
from .models import Employee


def employee_list(request):
    employees = Employee.objects.all()
    return JsonResponse({"employees": list(employees.values())})

@csrf_exempt
def employee_detail(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'GET':
        return JsonResponse({"employee": model_to_dict(employee)})
    elif request.method == 'POST':
        employee.first_name = request.POST.get('first_name')
        employee.last_name = request.POST.get('last_name')
        employee.email = request.POST.get('email')
        employee.position = request.POST.get('position')
        employee.save()
        return JsonResponse({"message": "Empleado actualizado"})
    elif request.method == 'DELETE':
        employee.delete()
        return JsonResponse({"message": "Empleado eliminado"})

@csrf_exempt
def employee_create(request):
    if request.method == 'POST':
        employee = Employee(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            position=request.POST.get('position')
        )
        employee.save()
        return JsonResponse({"message": "Empleado creado"})


@login_required
@admin_required
def manage_employees(request):
    # Lógica para manejar empleados
    pass


@login_required
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')  # Ajusta esta redirección según tu necesidad
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

@login_required
def edit_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employees/edit_employee.html', {'form': form})

@login_required
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        employee.delete()
        return redirect('admin_dashboard')
    return render(request, 'employees/delete_employee.html', {'employee': employee})