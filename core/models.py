from decimal import Decimal

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import F
from django.core.validators import MinValueValidator, MaxValueValidator

from proy_sales.utils import valida_cedula, phone_regex


class ActiveBrandManager(models.Manager):
    """
    Manager personalizado para obtener solo marcas activas (state=True).
    """
    def get_queryset(self):
        return super().get_queryset().filter(state=True)


class Brand(models.Model):
    """
    Representa una marca de productos.
    """
    description = models.CharField('Artículo', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    objects = models.Manager()
    active_brands = ActiveBrandManager()

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'
        ordering = ['description']
        indexes = [
            models.Index(fields=['description']),
        ]

    def __str__(self):
        return self.description


class Supplier(models.Model):
    """
    Representa un proveedor de productos.
    """
    name = models.CharField(max_length=100)
    ruc = models.CharField(max_length=13, validators=[valida_cedula])
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, validators=[phone_regex])
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['name']
        indexes = [models.Index(fields=['name']),]

    def __str__(self):
        return self.name


class ActiveProductManager(models.Manager):
    """
    Manager personalizado para obtener solo productos activos (state=True).
    """
    def get_queryset(self):
        return super().get_queryset().filter(state=True)


class Product(models.Model):
    """
    Representa un producto en el supermercado.
    """
    class Status(models.TextChoices):
        STORE = 'RS', 'Rio Store'
        FERRISARITO = 'FS', 'Ferrisariato'
        COMISARIATO = 'CS', 'Comisariato'

    description = models.CharField('Artículo', max_length=100)
    cost = models.DecimalField('Costo Producto', max_digits=10, decimal_places=2, default=Decimal('0.00'))
    price = models.DecimalField('Precio', max_digits=10, decimal_places=2, default=Decimal('0.00'), validators=[MinValueValidator(Decimal('0.01'))])  # Validación de precio positivo
    stock = models.PositiveIntegerField(default=100, help_text="Stock debe estar en 0 y 10000 unidades", verbose_name='Stock', validators=[MaxValueValidator(10000)])  # Validación de stock máximo
    iva = models.IntegerField(verbose_name='IVA', choices=((0, '0%'), (5, '5%'), (15, '15%')), default=15)
    expiration_date = models.DateTimeField('Fecha Caducidad', default=timezone.now)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products', verbose_name='Marca')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, verbose_name='Proveedor')
    categories = models.ManyToManyField('Category', verbose_name='Categoría')
    line = models.CharField('Linea', max_length=2, choices=Status.choices, default=Status.COMISARIATO)
    image = models.ImageField(upload_to='products/', blank=True, null=True, default='products/default.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    objects = models.Manager()
    active_products = ActiveProductManager()

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['description']
        indexes = [models.Index(fields=['description']),]

    def __str__(self):
        return self.description

    @property
    def get_categories(self):
        return " - ".join([c.description for c in self.categories.all().order_by('description')])

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError("No hay suficiente stock disponible.")
        self.stock = F('stock') - quantity
        self.save()

    def update_stock(self, id, quantity):
        Product.objects.filter(pk=id).update(stock=F('stock') - quantity)


class Category(models.Model):
    """
    Representa una categoría de productos.
    """
    description = models.CharField(verbose_name='Categoría', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['description']
        indexes = [models.Index(fields=['description']),]

    def __str__(self):
        return self.description


class Customer(models.Model):
    """
    Representa un cliente del supermercado.
    """
    dni = models.CharField(verbose_name='DNI', max_length=13, unique=True, blank=True, null=True)
    first_name = models.CharField(verbose_name='Nombres', max_length=50)
    last_name = models.CharField(verbose_name='Apellidos', max_length=50)
    address = models.TextField(verbose_name='Dirección', blank=True, null=True)
    gender = models.CharField(verbose_name='Sexo', max_length=1, choices=(('M', 'Masculino'), ('F', 'Femenino')), default='M')
    date_of_birth = models.DateField(verbose_name='Fecha Nacimiento', blank=True, null=True)
    phone = models.CharField(verbose_name='Teléfono', max_length=50, blank=True, null=True)
    email = models.CharField(verbose_name='Correo', max_length=100, blank=True, null=True)
    image = models.ImageField(verbose_name='Foto', upload_to='customers/', blank=True, null=True, default='products/default.png')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField(verbose_name='Activo', default=True)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['last_name']
        indexes = [models.Index(fields=['last_name']),]

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super().save(*args, **kwargs)

    @property
    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class PaymentMethod(models.Model):
    """
    Representa un método de pago aceptado por el supermercado.
    """
    description = models.CharField(verbose_name='Método Pago', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = 'Método de Pago'
        verbose_name_plural = 'Métodos de Pagos'
        ordering = ['description']

    def __str__(self):
        return self.description


class Invoice(models.Model):
    """
    Representa una factura de venta.
    """
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='customer_invoices', verbose_name='Cliente')
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT, related_name='payment_invoices', verbose_name='Método pago')
    issue_date = models.DateTimeField(verbose_name='Fecha Emisión', default=timezone.now)
    subtotal = models.DecimalField(verbose_name='Subtotal', default=0, max_digits=16, decimal_places=2)
    iva = models.DecimalField(verbose_name='IVA', default=0, max_digits=16, decimal_places=2)
    discount = models.DecimalField(verbose_name='Descuento', default=0, max_digits=16, decimal_places=2)
    total = models.DecimalField(verbose_name='Total', default=0, max_digits=16, decimal_places=2)
    payment = models.DecimalField(verbose_name='Pago', default=0, max_digits=16, decimal_places=2)
    change = models.DecimalField(verbose_name='Cambio', default=0, max_digits=16, decimal_places=2)
    status = models.CharField(verbose_name='Estado', max_length=1, choices=(('F', 'Factura'), ('A', 'Anulada'), ('D', 'Devolución')), default='F')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    state = models.BooleanField('Activo', default=True)

    class Meta:
        verbose_name = "Factura"
        verbose_name_plural = "Facturas"
        ordering = ('-issue_date', 'customer',)
        indexes = [
            models.Index(fields=['issue_date']),
            models.Index(fields=['customer']),
        ]

    def __str__(self):
        return f"{self.id} - {self.customer}"


class InvoiceDetail(models.Model):
    """
    Representa un detalle (línea) de una factura de venta.
    """
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='details', verbose_name='Factura')  # Corregido related_name
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Producto')
    cost = models.DecimalField(default=0, max_digits=16, decimal_places=2, null=True, blank=True)
    quantity = models.DecimalField(default=0, max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])  # Validación de cantidad positiva
    price = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    subtotal = models.DecimalField(default=0, max_digits=16, decimal_places=2)
    iva = models.DecimalField(default=0, max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Factura Detalle"
        verbose_name_plural = "Factura Detalles"
        ordering = ('id',)
        indexes = [models.Index(fields=['id']),]

    def __str__(self):
        return f"{self.product} (Factura #{self.invoice.id})"
