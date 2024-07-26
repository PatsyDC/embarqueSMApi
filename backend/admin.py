#------------Usuarios--------------------
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('dni', 'nombrey_apellido', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('dni', 'password')}),
        ('Información Personal', {'fields': ('nombrey_apellido', 'jefe_inmediato', 'cargo', 'area', 'idgeneral')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('dni', 'nombrey_apellido', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('dni',)
    ordering = ('dni',)

admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(DiarioDePesca)