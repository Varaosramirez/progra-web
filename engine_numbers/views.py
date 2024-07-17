# engine_numbers/views.py
from django.http import JsonResponse

def example_view(request):
    return JsonResponse({"message": "Esta es una vista de ejemplo de la aplicación engine_numbers"})
