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
from django.conf import settings  # Importa la configuración del proyecto
from django.conf.urls.static import static  # Importa la función para servir archivos estáticos en desarrollo
from django.contrib import admin
from django.urls import path, include
from core import views  # Importa las vistas de tu app 'core'

urlpatterns = [
    # URLs de la aplicación de administración de Django
    path('admin/', admin.site.urls),

    # URLs de la aplicación principal (core)
    path('', views.home, name='home'),  # URL de la página de inicio
    path('signup/', views.signup, name='signup'),  # URL de registro de usuario
    path('login/', views.CustomLoginView.as_view(), name='login'),  # URL de inicio de sesión

    # Incluye las URLs de la aplicación 'core' en un espacio de nombres llamado 'core'
    path('', include('core.urls', namespace='core')),
]

# Sirve archivos estáticos (CSS, JavaScript, Imágenes) en modo DEBUG (desarrollo)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

