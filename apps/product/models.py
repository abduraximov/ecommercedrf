from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_("Category name"))
    image = models.ImageField(upload_to="category_images/", verbose_name=_("Category Image"), blank=True, null=True)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="subcategories",
        verbose_name=_("Parent Category"),
    )
    main = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Brand Name"))

    class Meta:
        verbose_name = _("Brand")
        verbose_name_plural = _("Brands")

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Feature Name"))

    class Meta:
        verbose_name = _("Feature")
        verbose_name_plural = _("Features")

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=100, verbose_name=_("Condition Name"))

    class Meta:
        verbose_name = _("Condition")
        verbose_name_plural = _("Conditions")

    def __str__(self):
        return self.name


class Product(BaseModel):
    name = models.CharField(max_length=200, verbose_name=_("Product Name"))
    description = RichTextUploadingField(verbose_name=_("Product Description"))
    is_recommend = models.BooleanField(default=False, verbose_name=_("Is Recommended"))
    seller_profile = models.ForeignKey(
        "user.SellerProfile", on_delete=models.CASCADE, verbose_name=_("Product seller"), related_name="products"
    )
    category = models.ForeignKey(
        "product.Category", on_delete=models.CASCADE, related_name="products", verbose_name=_("Category")
    )
    brand = models.ForeignKey(
        "product.Brand",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name=_("Brand"),
        related_name="products",
    )
    features = models.ManyToManyField(
        "product.Feature", blank=True, verbose_name=_("Features"), related_name="products"
    )
    conditions = models.ManyToManyField(
        "product.Condition", blank=True, verbose_name=_("Conditions"), related_name="products"
    )

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=50, verbose_name=_("Color Name"))

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to="product_images/", verbose_name=_("Image"))
    is_main = models.BooleanField(default=False, verbose_name=_("Main image"))

    def __str__(self):
        return self.image.name


class ProductType(BaseModel):
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, verbose_name=_("Product"), related_name="stock"
    )
    color = models.ForeignKey(
        "product.Color",
        on_delete=models.SET_NULL,
        verbose_name=_("Product color"),
        related_name="product_stocks",
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=18, decimal_places=2, validators=[MinValueValidator(0)], verbose_name=_("Price")
    )
    sale_price = models.DecimalField(
        max_digits=18,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(0)],
        verbose_name=_("Sale price"),
    )
    images = models.ManyToManyField(
        "product.ProductImage", verbose_name=_("Product images"), related_name="product_stocks"
    )

    class Meta:
        verbose_name = _("Product type")
        verbose_name_plural = _("Products type")


class ProfitPrice(models.Model):
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="profit_prices", verbose_name=_("Product")
    )
    min_quantity = models.PositiveIntegerField(verbose_name=_("Minimum Quantity"))
    max_quantity = models.PositiveIntegerField(verbose_name=_("Maximum Quantity"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))

    class Meta:
        verbose_name = _("Profit price")
        verbose_name_plural = _("Profit prices")

    def __str__(self):
        return f"{self.product.name} - {self.min_quantity} to {self.max_quantity} pcs"
