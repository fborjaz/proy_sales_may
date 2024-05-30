from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from rest_framework import viewsets, permissions
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth.views import LoginView, LogoutView

from core.forms import ProductForm
from core.models import Product, Brand, Supplier, Category
from core.serializers import ProductSerializer, BrandSerializer, SupplierSerializer, CategorySerializer

# ------------------------------------------------------------------------------
# Vistas Generales
# ------------------------------------------------------------------------------

def home(request):
    data = {
        "title1": "Autor | TeacherCode",
        "title2": "Super Mercado Economico"
    }
    return render(request, 'core/home.html', data)

# ------------------------------------------------------------------------------
# ViewSets
# ------------------------------------------------------------------------------
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ------------------------------------------------------------------------------
# Vistas de Productos
# ------------------------------------------------------------------------------
@login_required
def product_list(request):
    data = {
        "title1": "Productos",
        "title2": "Consulta De Productos"
    }
    products = Product.objects.all()
    data["products"] = products
    return render(request, "core/products/list.html", data)


@login_required
def product_create(request):
    data = {"title1": "Productos", "title2": "Ingreso De Productos"}
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado exitosamente')
            return redirect('core:product_list')
    else:
        data["form"] = ProductForm()
    return render(request, "core/products/form.html", data)


@login_required
def product_update(request, id):
    data = {"title1": "Productos", "title2": ">Edición De Productos"}
    product = Product.objects.get(pk=id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect("core:product_list")
    else:
        form = ProductForm(instance=product)
        data["form"] = form
    return render(request, "core/products/form.html", data)


@login_required
def product_delete(request, id):
    product = Product.objects.get(pk=id)
    data = {"title1": "Eliminar", "title2": "Eliminar Un Producto", "product": product}
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Producto eliminado exitosamente')
        return redirect("core:product_list")

    return render(request, "core/products/delete.html", data)


# ------------------------------------------------------------------------------
# Vistas de Marcas
# ------------------------------------------------------------------------------

@login_required
def brand_list(request):
    data = {
        "title1": "Marcas",
        "title2": "Consulta De Marcas De Productos"
    }
    brands = Brand.objects.all()
    data["brands"] = brands
    return render(request, "core/brands/list.html", data)

# ------------------------------------------------------------------------------
# Vistas de Proveedores
# ------------------------------------------------------------------------------

@login_required
def supplier_list(request):
    data = {
        "title1": "Proveedores",
        "title2": "Consulta De proveedores"
    }
    suppliers = Supplier.objects.all()
    data["suppliers"] = suppliers
    return render(request, "core/suppliers/list.html", data)


# ------------------------------------------------------------------------------
# Vistas de Categorías
# ------------------------------------------------------------------------------

@login_required
def category_list(request):
    data = {
        "title1": "Categoria",
        "title2": "Consulta De Categoria"
    }
    categories = Category.objects.all()
    data["categories"] = categories
    return render(request, "core/categorys/list.html", data)


# ------------------------------------------------------------------------------
# Vistas de Autenticación
# ------------------------------------------------------------------------------

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect(reverse('login'))
            except IntegrityError:
                messages.error(request, 'El nombre de usuario ya está en uso.')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        messages.success(self.request, '¡Bienvenido!')
        return super().form_valid(form)

    def get_success_url(self):
        if self.request.user.is_staff:
            return '/admin/'
        else:
            return '/'

class CustomLogoutView(LogoutView):
    template_name = 'base.html'

    def get_next_page(self):
        return reverse('home')

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, '¡Hasta pronto!')
        return super().dispatch(request, *args, **kwargs)