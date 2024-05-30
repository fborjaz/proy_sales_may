from django.urls import path
from core import views

from core.views import CustomLogoutView

app_name = 'core'

urlpatterns = [
    # URLs de productos
    path('product_list/', views.product_list, name='product_list'),
    path('product_create/', views.product_create, name='product_create'),
    path('product_update/<int:id>/', views.product_update, name='product_update'),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete'),

    # URLs de marcas
    path('brand_list/', views.brand_list, name='brand_list'),

    # URLs de proveedores
    path('supplier_list/', views.supplier_list, name='supplier_list'),

    # URLs de categorías
    path('category_list/', views.category_list, name='category_list'),

    # Cerrado de sesión
    path('logout/', CustomLogoutView.as_view(), name='logout'),

]
