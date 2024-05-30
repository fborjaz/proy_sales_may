"""
URL configuration for proy_sales project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# proy_sales/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views
from core.views import home, signup, CustomLoginView, CustomLogoutView # Importa las vistas de la aplicación core

urlpatterns = [
    # URLs de la aplicación de administración de Django
    path('admin/', admin.site.urls),

    # URLs de la aplicación principal (core)
    path('', views.home, name='home'),  # URL de la página de inicio
    path('signup/', views.signup, name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),  # URL de inicio de sesión
    path('logout/', CustomLogoutView.as_view(), name='logout'), # URL de cierre de sesión

    # Incluye las URLs de la aplicación 'core' en un espacio de nombres llamado 'core'
    path('core/', include('core.urls')),
]

# Sirve archivos estáticos (CSS, JavaScript, Imágenes) en modo DEBUG (desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

