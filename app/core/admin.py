"""
Django admin customization.
"""
from core.models import Ingredient, Recipe, Tag, User
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Permission
from django.utils.translation import gettext_lazy as _
from patrimonio.models import Patrimonio


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['id', 'email', 'name']
    fieldsets = (
        (_('Personal Info'), {'fields': ('name', 'email', 'password',)}),
        (_('Groups'), {'fields': ('groups',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    filter_horizontal = ('groups',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            ),
        }),
    )


class LightAdmin(ModelAdmin):
    list_per_page = 5
    list_filter = []


class AutoCompleteAdmin(LightAdmin):
    autocomplete_fields = ['setor', 'responsavel']
    raw_id_fields = ()


class IngredientAdmin(LightAdmin):
    search_fields = ['name']


admin.site.register(Ingredient, IngredientAdmin)

admin.site.register(User, UserAdmin)
admin.site.register(Recipe, LightAdmin)
admin.site.register(Tag, LightAdmin)
admin.site.register(Patrimonio, AutoCompleteAdmin)
admin.site.register(Permission, LightAdmin)
