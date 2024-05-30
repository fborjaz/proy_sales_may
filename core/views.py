from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ProductForm
from .models import Product, Brand, Supplier, Category

# ------------------------------------------------------------------------------
# Vistas Generales
# ------------------------------------------------------------------------------

def home(request):
    data = {
        "title1": "Autor | TeacherCode",
        "title2": "Super Mercado Economico"
    }
    return render(request, 'core/home.html', data)

@login_required
def signout(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')

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
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('core:product_list')
            except IntegrityError:
                messages.error(request, 'El nombre de usuario ya está en uso.')
        else:
            messages.error(request, 'Error al procesar el formulario.')
        return render(request, 'signup.html', {"form": form})

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')