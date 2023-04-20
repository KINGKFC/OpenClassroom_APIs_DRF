from rest_framework.serializers import ModelSerializer

from shop.models import Category, Product, Article

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'date_created', 'date_updated', 'name', 'category']


class CategorySerializer(ModelSerializer):

    products = ProductSerializer(many=True)
    class Meta:
        model = Category
        fields = ['id', 'date_created', 'date_updated', 'name', 'products']


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'date_created', 'date_updated', 'name', 'price', 'product']