from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from apps.product.filters import ProductFilter
from apps.product.models import Category, Product
from apps.product.serializers import (CategoryProductsSerializer,
                                      MainCategorySerializer,
                                      PopularCategorySerializer,
                                      ProductDetailSerializer,
                                      RecommendProductsSerializer)


class MainCategoryAPIView(generics.ListAPIView):
    serializer_class = MainCategorySerializer

    def get_queryset(self):
        return Category.objects.filter(main=True)


class PopularCategoryAPIView(generics.ListAPIView):
    serializer_class = PopularCategorySerializer

    def get_queryset(self):
        return Category.objects.filter(main=True)


class RecommendProductsAPIView(generics.ListAPIView):
    serializer_class = RecommendProductsSerializer

    def get_queryset(self):
        return Product.objects.filter(is_recommend=True)


class CategoryProductsAPIView(generics.ListAPIView):
    serializer_class = CategoryProductsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

    def get_queryset(self):
        slug = self.kwargs.get("slug", None)
        data = Product.objects.filter(category__slug=slug)
        return data


class ProductDetailAPIView(generics.RetrieveAPIView):
    serializer_class = ProductDetailSerializer
    queryset = Product.objects.all()
    lookup_field = "pk"
