from django.contrib import admin
from apps.user.models import Profile, SellerProfile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user"
    )


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "company_name"
    )



