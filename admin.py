from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Permission

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    """
    Custom admin for CustomUser model.
    """

    list_display = ("email", "name", "is_staff", "last_login")
    search_fields = ("email", "name")
    list_filter = ("is_staff", "is_superuser", "groups")

    # Define the fieldsets for user details in the admin
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name",)}),
        ("Permissions", {
            "fields": (
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions"
            )
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # Define the fields for adding a new user in the admin
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "name",
                "is_staff",
                "is_active"
            ),
        }),
    )

    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions")
    readonly_fields = ("last_login", "date_joined")

# Register the CustomUser model with the CustomUserAdmin configuration
admin.site.register(CustomUser, CustomUserAdmin)

# Uncomment the following line if you need to manage permissions through the admin interface
# admin.site.register(Permission)
