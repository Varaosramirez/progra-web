from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import admin_dashboard, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('employees/', include('employees.urls')),
    path('sales/', include('sales.urls')),
    path('cart/', include('cart.urls')),
    path('engine_numbers/', include('engine_numbers.urls')),
    path('', home, name='home'),  # Definir la URL para la vista 'home'
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
