from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from vehicles.models import Vehicle
from django.contrib import messages


@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user, completed=False)
    items = cart.items.all()
    total = sum(item.vehicle.price * item.quantity for item in items)
    context = {
        'items': items,
        'total': total
    }
    return render(request, 'cart/cart.html', context)
@login_required
def add_to_cart(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, vehicle=vehicle)
    if created:
        cart.items.add(cart_item)
        messages.success(request, "Vehículo agregado al carrito.")
    else:
        cart_item.quantity += 1
        cart_item.save()
        messages.info(request, "Cantidad del vehículo actualizada en el carrito.")
    return redirect('vehicle_list')

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, cart__user=request.user, cart__completed=False)
    cart_item.delete()
    return redirect('cart_detail')


@login_required
def finalize_purchase(request):
    cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    if not cart.items.exists():
        messages.error(request, "No hay artículos en el carrito.")
        return redirect('view_cart')
    cart.completed = True
    cart.save()
    messages.success(request, "Compra finalizada con éxito.")
    return redirect('vehicle_list')

@login_required
def purchase_success(request):
    return render(request, 'cart/purchase_success.html')

@login_required
def cart_detail(request):
    cart = get_object_or_404(Cart, user=request.user, completed=False)
    items = cart.cart_items.all()
    total = sum(item.vehicle.price * item.quantity for item in items)
    return render(request, 'cart/cart.html', {'items': items, 'total': total})
