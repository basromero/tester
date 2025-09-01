from django.contrib import admin
from .models import Cliente, Empleado, Categoria, Producto, Orden, DetalleOrden, Proveedor

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'cli_nombre', 'cli_ciudad', 'cli_pais', 'cli_mail')
    search_fields = ('cli_nombre', 'cli_ciudad', 'cli_pais')

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('id_empleado', 'emp_nombre', 'emp_apellido', 'emp_mail', 'emp_fecha_nac')
    search_fields = ('emp_nombre', 'emp_apellido', 'emp_mail')

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'cat_nombre')
    search_fields = ('cat_nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'pro_nombre', 'id_categoria', 'pro_precio', 'pro_stock')
    list_filter = ('id_categoria',)
    search_fields = ('pro_nombre',)

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'id_cliente', 'id_empleado', 'ord_fecha')
    list_filter = ('ord_fecha',)
    search_fields = ('id_cliente__cli_nombre', 'id_empleado__emp_nombre')

@admin.register(DetalleOrden)
class DetalleOrdenAdmin(admin.ModelAdmin):
    list_display = ('id_detord', 'id_producto', 'deo_precio', 'deo_cantidad', 'id_orden')
    search_fields = ('id_producto__pro_nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id_proveedor', 'prv_empresa', 'prv_contacto', 'prv_telefono')
    search_fields = ('prv_empresa', 'prv_contacto')

