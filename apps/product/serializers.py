from django.db.models import Min, Avg
from rest_framework import serializers

from apps.common.models import Review
from apps.product.models import Category, Product, ProductType


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "main")


class ParentCategorySerializer(serializers.ModelSerializer):
    min_price_product = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ("id", "name", "image", "main", "min_price_product")

    def get_min_price_product(self, obj):
        product_types = ProductType.objects.filter(product__category=obj)
        min_price = product_types.aggregate(min_price=Min("price"))["min_price"]
        return min_price


class PopularCategorySerializer(serializers.ModelSerializer):
    subcategories = ParentCategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ("id", "name", "image", "subcategories", "main")


class ImageSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()


class RecommendProductsSerializer(serializers.ModelSerializer):
    category = MainCategorySerializer()
    product_type = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("id", "name", "category", "product_type")

    def get_product_type(self, obj):
        product_types = ProductType.objects.filter(product=obj)
        data = {}

        if product_types.exists():
            product_type = product_types.first()
            if product_type.images.exists():
                image_serializer = ImageSerializer(product_type.images.first())
                data["image"] = image_serializer.data
            else:
                data["image"] = None
            data["price"] = product_types.aggregate(min_price=Min("price"))["min_price"]
        else:
            data["image"] = None
            data["price"] = None

        return data


class CategoryProductsSerializer(serializers.ModelSerializer):
    product_type = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "description",
            "seller_profile",
            "category",
            "brand",
            "features",
            "conditions",
            "product_type",
            "reviews"
        )

    def get_product_type(self, obj):
        product_types = ProductType.objects.filter(product=obj)
        data = {}
        data["count_products"] = product_types.count()
        if product_types.exists():
            product_type = product_types.first()
            if product_type.images.exists():
                image_serializer = ImageSerializer(product_type.images.first())
                data["image"] = image_serializer.data
            else:
                data["image"] = None
            data["price"] = product_type.price
            if product_type.sale_price:
                data["sale_price"] = product_type.sale_price
        else:
            data["image"] = None
            data["price"] = None

        return data

    def get_reviews(self, obj):
        review = Review.objects.filter(product=obj)
        data = {
            "count_review": review.count(),
            "avarege_rating": review.aggregate(avg_rate=Avg("rating"))["avg_rate"]
        }
        return data
