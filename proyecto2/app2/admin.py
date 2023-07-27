from django.contrib import admin
from app2.models import usuarios, productos, pedidos
# Register your models here.

class usuario_admin(admin.ModelAdmin):
    list_display = ('nombre','pais','email')
    search_fields = ('nombre','pais')

class productos_admin(admin.ModelAdmin):
    list_display = ('nombre','categoria','precio','proveedor')
    list_filter = ('categoria',)

admin.site.register(usuarios,usuario_admin)
admin.site.register(productos, productos_admin)
admin.site.register(pedidos)

