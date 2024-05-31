from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm,PasswordEditlForm
from .forms import BrandForm
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView

from core.forms import ProductForm, CategoryForm, BrandForm, SupplierForm
from core.models import Product, Brand, Supplier, Category

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
            product = form.save(commit=False)  # Crea el producto pero no lo guarda aún
            product.user = request.user  # Asigna el usuario actual al producto
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
def brand_List(request):
    data = {
        'title1': 'Marcas',
        'title2': 'Consulta de marcas'
    }
    brands = Brand.objects.filter(user=request.user) # select * from brand
    data['brands'] = brands
    return render(request, 'core/brands/list.html', data)

@login_required
def brand_create(request):
    data = {'title1': 'Marcas','title2': 'Ingreso de marcas'}

    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.user = request.user
            brand.save()
            return redirect('core:brand_list')
    else:
        data['form'] = BrandForm() # controles formulario sin datos

    return render(request, 'core/brands/form.html', data)

@login_required
def brand_update(request, id):
    data = {'title1': 'Marcas','title2': 'Edición de marcas'}
    brand = Brand.objects.get(pk=id)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('core:brand_list')
    else:
        form = BrandForm(instance=brand)
        data['form'] = form

    return render(request, 'core/brands/form.html', data)

@login_required
def brand_delete(request, id):
    brand = Brand.objects.get(pk=id)
    data = {'title1': 'Marcas','title2': 'Eliminar una marca','brand': brand}
    if request.method == 'POST':
        brand.delete()
        return redirect('core:brand_list')

    return render(request, 'core/brands/delete.html', data)

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
                return redirect('home')
            except IntegrityError:
                messages.error(request, 'El nombre de usuario ya está en uso.')
        else:
            messages.error(request, 'Error al procesar el formulario.')
        return render(request, 'signup.html', {"form": form})

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {"form": form})

# Vista de inicio de sesión para la aplicación
class AppLoginView(LoginView):
    template_name = 'signin.html'
    success_url = reverse_lazy('home')

# Vista de inicio de sesión para el panel de administración
class AdminLoginView(LoginView):
    template_name = 'admin/login.html'  # Utiliza la plantilla por defecto de Django admin

def signin(request):
    data = {"title1": "Productos", "title2": "Ingreso De"}
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
    return render(request, 'signin.html',{'form': form},data)


def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('home')

# ------------------------------------------------------------------------------
# Vistas de Perfil
# ------------------------------------------------------------------------------

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        password_form = PasswordEditlForm(request.user, request.POST)
        if user_form.is_valid() and password_form.is_valid():
            user_form.save()
            password_form.save()
            messages.success(request, 'Perfil actualizado exitosamente.')
            return redirect('profile')
    else:
        user_form = UserEditForm(instance=request.user)
        password_form = PasswordEditlForm(request.user)
    context = {
        'user_form': user_form,
        'password_form':password_form,
    }
    return render(request, 'profile.html', context)
