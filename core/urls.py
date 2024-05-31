from django.urls import path
from core import views

from django.contrib.auth.views import LogoutView

app_name = 'core'

urlpatterns = [
    # URLs de productos
    path('product_list/', views.product_list, name='product_list'),
    path('product_create/', views.product_create, name='product_create'),
    path('product_update/<int:id>/', views.product_update, name='product_update'),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete'),

    # URLs de marcas
    path('brands_list/', views.brand_List, name='brands_list'),
    path('brand_create/', views.brand_create, name='brand_create'),
    path('brand_update/<int:id>/', views.brand_update, name='brand_update'),
    path('brand_delete/<int:id>/', views.brand_delete, name='brand_delete'),

    # URLs de proveedores
    path('supplier_list/', views.supplier_list, name='supplier_list'),

    # URLs de categorías
    path('category_list/', views.category_list, name='category_list'),
  # Cerrado de sesión
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
