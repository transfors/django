from django.contrib import admin
from app4.models import usuario

# Register your models here.
class usuario_admin(admin.ModelAdmin):
    list_display = ('nombre','ciudad','carrera')
    # es una tupla
    search_fields = ('ciudad',)

admin.site.register(usuario,usuario_admin)



