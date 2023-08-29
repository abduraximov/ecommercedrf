from django.contrib import admin

from apps.product.models import (Brand, Category, Color, Condition, Feature,
                                 Product, ProductImage, ProductType,
                                 ProfitPrice)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ("id", "name", "slug")


@admin.register(Brand, Feature, Condition, Color)
class ListAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "seller_profile")


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image",
    )


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "price")


@admin.register(ProfitPrice)
class ProfitPriceAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "product",
    )
