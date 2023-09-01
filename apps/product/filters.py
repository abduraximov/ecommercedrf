from django_filters import BooleanFilter, FilterSet, NumberFilter
from django_filters.rest_framework import BaseInFilter
from rest_framework import filters


class ListFilter(BaseInFilter, filters.BaseFilterBackend):
    pass


class ProductFilter(FilterSet):
    price_from = NumberFilter(method="filter_price_from")
    price_to = NumberFilter(method="filter_price_to")
    brand = ListFilter(field_name="brand", lookup_expr="in")
    features = ListFilter(field_name="features", lookup_expr="in")

    rating_equals = NumberFilter(method="filter_rating_equals")

    seller_verified = BooleanFilter(field_name="seller_profile__is_verified")

    def filter_price_from(self, queryset, name, value):
        return queryset.filter(stock__price__gte=value)

    def filter_price_to(self, queryset, name, value):
        return queryset.filter(stock__price__lte=value)

    def filter_rating_equals(self, queryset, name, value):
        return queryset.filter(reviews__rating=value)
