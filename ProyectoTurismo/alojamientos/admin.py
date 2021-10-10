from django.contrib import admin
from .models import Categoria, Alojamiento, Post

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class AlojamientoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')
    
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Alojamiento, AlojamientoAdmin)
admin.site.register(Post, PostAdmin)
