from django.urls import path

from apps.product import views

urlpatterns = [
    path("categories/", views.MainCategoryAPIView.as_view(), name="categories"),
    path(
        "categories/popular/",
        views.PopularCategoryAPIView.as_view(),
        name="popular_categories",
    ),
    path(
        "category/<slug:slug>/products/",
        views.CategoryProductsAPIView.as_view(),
        name="category_products",
    ),
    path(
        "recommend/",
        views.RecommendProductsAPIView.as_view(),
        name="recommend_products",
    ),
    path("<int:pk>/detail/", views.ProductDetailAPIView.as_view(), name="product_detail"),
]
