from django.contrib import admin

from apps.common.models import Card, Order, Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "profile", "rating")
    list_filter = ("product", "profile")
    search_fields = ("product__name", "profile__user__username")


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("product", "profile", "quantity", "is_active")
    list_filter = ("product", "profile", "is_active")
    search_fields = ("product__name", "profile__user__username")


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("card", "profile", "price")
    list_filter = ("card__product", "profile")
    search_fields = ("card__product__name", "profile__user__username")
