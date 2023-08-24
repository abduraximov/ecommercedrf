from django.db import models
from apps.common.models import BaseModel
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from apps.user.choices import GenderTypes
from ckeditor_uploader.fields import RichTextUploadingField


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(verbose_name=_("Avatar"), upload_to="profile/pictures", null=True, blank=True)
    address = models.CharField(verbose_name=_("Address"), max_length=255, null=True, blank=True)
    postal_code = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(
        verbose_name=_("Gender"),
        choices=GenderTypes.choices,
        max_length=15,
        null=True,
    )

    def __str__(self):
        return self.user.username


class SellerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="seller_profile")
    company_name = models.CharField(max_length=100, verbose_name=_("Company name"))
    description = RichTextUploadingField(verbose_name=_("Description"))
    contact_info = models.CharField(max_length=200)
    company_photo = models.ImageField(upload_to='seller_profile/pictures', blank=True, null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
