from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, DiarioDePesca

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('dni', 'nombrey_apellido', 'tipo_usurio', 'cargo', 'area', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'tipo_usurio',)  # Agregado tipo_usurio a los filtros
    fieldsets = (
        (None, {'fields': ('dni', 'password')}),
        ('Información Personal', {'fields': ('nombrey_apellido', 'cargo', 'area', 'idgeneral', 'tipo_usurio')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('dni', 'nombrey_apellido', 'password1', 'password2', 'is_staff', 'is_active', 'tipo_usurio', 'cargo', 'area')}
        ),
    )
    search_fields = ('dni', 'nombrey_apellido',)
    ordering = ('dni',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(DiarioDePesca)
