from django.urls import path, include
from rest_framework import routers
from core import views

app_name = 'core'  # Define el nombre de la aplicación 'core'

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='product')
router.register(r'brands', views.BrandViewSet, basename='brand')
router.register(r'suppliers', views.SupplierViewSet, basename='supplier')
router.register(r'categories', views.CategoryViewSet, basename='category')

urlpatterns = [
    path('', views.home, name='home'),  # Asegúrate de tener la función home definida
    path('', include(router.urls)),
]
