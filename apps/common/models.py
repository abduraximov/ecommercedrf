from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created_at"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated_at"))

    class Meta:
        abstract = True


class Review(BaseModel):
    product = models.ForeignKey(
        "product.Product", on_delete=models.CASCADE, related_name="reviews", verbose_name=_("Product")
    )
    profile = models.ForeignKey(
        "user.Profile", on_delete=models.CASCADE, related_name="reviews", verbose_name=_("Profile")
    )
    text = models.TextField(verbose_name=_("Review Text"))
    rating = models.PositiveSmallIntegerField(
        verbose_name=_("Rating"), validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ("product", "profile")
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        return f"Review for {self.product} by {self.profile.user}"


class Card(BaseModel):
    product = models.ForeignKey(
        "product.ProductType", on_delete=models.CASCADE, related_name="cards", verbose_name=_("Product")
    )
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name=_("Quantity"))
    profile = models.ForeignKey(
        "user.Profile", on_delete=models.CASCADE, related_name="cards", verbose_name=_("Profile")
    )
    is_active = models.BooleanField(default=True, verbose_name=_("Active"))

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    def __str__(self):
        return f"{self.profile.user.username}'s {self.quantity} {self.product.name}(s)"


class Order(BaseModel):
    card = models.ForeignKey("common.Card", on_delete=models.CASCADE, related_name="orders", verbose_name=_("Card"))
    profile = models.ForeignKey(
        "user.Profile", on_delete=models.CASCADE, related_name="orders", verbose_name=_("Profile")
    )
    price = models.DecimalField(
        max_digits=18, decimal_places=2, validators=[MinValueValidator(0)], verbose_name=_("Price")
    )
