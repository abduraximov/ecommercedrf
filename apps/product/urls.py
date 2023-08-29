from django.urls import path

from apps.product.views import (MainCategoryAPIView, PopularCategoryAPIView,
                                RecommendProductsAPIView)

urlpatterns = [
    path("categories/", MainCategoryAPIView.as_view(), name="categories"),
    path("categories/popular/", PopularCategoryAPIView.as_view(), name="popular_categories"),
    path("recommend/", RecommendProductsAPIView.as_view(), name="recommend_products"),
]
