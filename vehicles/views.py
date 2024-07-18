from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from .models import Vehicle
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from users.decorators import admin_required
from .forms import VehicleForm
from .models import Vehicle


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

@csrf_exempt
@login_required
def vehicle_detail(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    if request.method == 'GET':
        return JsonResponse({"vehicle": model_to_dict(vehicle)})
    elif request.method == 'POST':
        vehicle.brand = request.POST.get('brand')
        vehicle.model = request.POST.get('model')
        vehicle.price = request.POST.get('price')
        vehicle.description = request.POST.get('description')
        vehicle.save()
        return JsonResponse({"message": "Vehículo actualizado"})
    elif request.method == 'DELETE':
        vehicle.delete()
        return JsonResponse({"message": "Vehículo eliminado"})

@csrf_exempt
def vehicle_create(request):
    if request.method == 'POST':
        vehicle = Vehicle(
            brand=request.POST.get('brand'),
            model=request.POST.get('model'),
            price=request.POST.get('price'),
            description=request.POST.get('description')
        )
        vehicle.save()
        return JsonResponse({"message": "Vehículo creado"})


@login_required
@admin_required
def manage_vehicles(request):
    # Lógica para manejar vehículos
    pass

@login_required
def add_vehicle(request):
    if not request.user.is_admin:
        return redirect('vehicle_list')

    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/add_vehicle.html', {'form': form})

@login_required
def edit_vehicle(request, vehicle_id):
    if not request.user.is_admin:
        return redirect('vehicle_list')

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'vehicles/edit_vehicle.html', {'form': form})

@login_required
def delete_vehicle(request, vehicle_id):
    if not request.user.is_admin:
        return redirect('vehicle_list')

    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.delete()
    return redirect('vehicle_list')