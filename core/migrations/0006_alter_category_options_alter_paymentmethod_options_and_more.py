# Generated by Django 4.2 on 2024-05-31 05:22

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_product_supplier'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['description'], 'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='paymentmethod',
            options={'ordering': ['description'], 'verbose_name': 'Método de Pago', 'verbose_name_plural': 'Métodos de Pagos'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Artículo'),
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='dni',
            field=models.CharField(blank=True, max_length=13, null=True, unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='Descuento'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='issue_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha Emisión'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='iva',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=16, verbose_name='IVA'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payment_invoices', to='core.paymentmethod', verbose_name='Método pago'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('F', 'Factura'), ('A', 'Anulada'), ('D', 'Devolución')], default='F', max_length=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='invoice',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='core.invoice', verbose_name='Factura'),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.product', verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='invoicedetail',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Método Pago'),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='core.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='core.category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100, verbose_name='Artículo'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))], verbose_name='Precio'),
        ),
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.PositiveIntegerField(default=100, help_text='Stock debe estar en 0 y 10000 unidades', validators=[django.core.validators.MaxValueValidator(10000)], verbose_name='Stock'),
        ),
    ]
