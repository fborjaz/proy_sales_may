from django.shortcuts import redirect, render, get_object_or_404
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
def brand_list(request):
    data = {
        'title1': 'Marcas',
        'title2': 'Consulta de marcas'
    }
    brands = Brand.objects.filter(user = request.user)
    data['brands'] = brands
    return render(request, 'core/brands/list.html', data)

#crear una marca
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
        data['form'] = BrandForm()

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
def supplier_List(request):
    data = {
        'title1': 'Proveedores',
        'title2': 'Consulta de proveedores'
    }
    suppliers = Supplier.objects.filter(user = request.user) # select * from supplier
    data['suppliers'] = suppliers
    return render(request, 'core/suppliers/list.html', data)

@login_required
def supplier_create(request):
    data = {"title1": "Proveedores", "title2": "Ingreso De Proveedores"}

    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.user = request.user  # Asigna el usuario actual
            supplier.save()
            messages.success(request, 'Proveedor actualizado exitosamente')
            return redirect('core:supplier_list')  # Redirige después de guardar
        else:
            # Si el formulario no es válido, muestra los errores en la plantilla
            messages.error(request, 'Error al crear el proveedor. Verifica los datos ingresados.')
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error en el campo {field}: {error}')

    else:  # Si es una solicitud GET, muestra el formulario vacío
        form = SupplierForm()

    data["form"] = form
    return render(request, "core/suppliers/form.html", data)

@login_required
def supplier_update(request, id):
    data = {"title1": "Proveedores", "title2": "Edición De Proveedores"}
    supplier = get_object_or_404(Supplier, pk=id)
    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proveedor actualizado exitosamente')
            return redirect("core:supplier_list")  # Redirigir después de guardar
    else:
        form = SupplierForm(instance=supplier)
        data["form"] = form
    return render(request, "core/suppliers/form.html", data)

@login_required
def supplier_delete(request, id):
    supplier = Supplier.objects.get(pk=id)
    data = {'title1': 'Proveedores','title2': 'Eliminar un proveedor','supplier': supplier}
    if request.method == 'POST':
        supplier.delete()
        return redirect('core:supplier_list')

    return render(request, 'core/suppliers/delete.html', data)


# ------------------------------------------------------------------------------
# Vistas de Categorías
# ------------------------------------------------------------------------------

@login_required
def category_list(request):
    data = {
        "title1": "Categorias",
        "title2": "Consulta De Categorias"
    }
    categories = Category.objects.filter(user = request.user)
    data["categories"] = categories
    return render(request, 'core/categorys/list.html', data)

@login_required
def category_create(request):
    data = {"title1": "Categoria", "title2": "Ingreso De Categorias"}

    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('core:category_list')
    else:
        data['form'] = CategoryForm

    return render(request, 'core/categorys/form.html', data)

@login_required
def category_update(request, id):
    data = {"title1": "Categorias", "title2": "Edicion De Categorias"}
    category = Category.objects.get(pk=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect("core:category_list")
    else:
        form = CategoryForm(instance=category)
        data["form"] = form
    return render(request, "core/categorys/form.html", data)

@login_required
def category_delete(request, id):
    category = Category.objects.get(pk=id)
    data = {"title1": "Eliminar", "title2": "Eliminar Una Categoria", "category": category}
    if request.method == "POST":
        category.delete()
        return redirect("core:category_list")

    return render(request, "core/categorys/delete.html", data)


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
