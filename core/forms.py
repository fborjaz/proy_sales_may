from django import forms
from core.models import Product, Category, Brand, Supplier
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=['description','price','stock','brand','categories','line','supplier','expiration_date','image','state']

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['description', 'state']


class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'ruc', 'address', 'phone', 'state']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['description', 'state']

class UserEditForm(UserChangeForm):
    password = None  # Excluimos el campo de contraseña del formulario de edición

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']  # Campos a editar

class PasswordEditlForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']