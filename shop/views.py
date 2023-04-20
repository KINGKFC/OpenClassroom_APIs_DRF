from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from shop.models import Category, Product, Article
from shop.serializers import CategorySerializer, ProductSerializer, ArticleSerializer


#class CategoryAPIView(APIView):
class CategoryAPIViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        # return Category.objects.all()
        # On renvoie seulement les catégories encore active en filtrant les catégories encore active
        return Category.objects.filter(active=True)

    # def get(self, *args, **kwargs):
    #     categories = Category.objects.all()
    #     serializer = CategorySerializer(categories, many=True)
    #     return Response(serializer.data)
    

# class ProductAPIView(APIView):
class ProductAPIViewset(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        # On recupère tous les produits encore actifs dans une variable nommée queryset
        queryset = Product.objects.filter(active=True)

        # On vérifie la présence du paramètre 'category_id' dans l'url et si oui alors nous appliquons notre filtre
        
        category_id = self.request.GET.get('category_id')
        # Si le paramètre existe dans l'url (donc not None)
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id) # Si oui on applique le filtre
        return queryset # On retourne l'élément queryset obtenu (filtre ou non filtrer)

        # return Product.objects.all()

    # def get(self, *args, **kwargs):
    #     products = Product.objects.all()
    #     serializer = ProductSerializer(products, many=True)
    #     return Response(serializer.data)


class ArticleAPIViewset(ReadOnlyModelViewSet):
    
    serializer_class = ArticleSerializer

    def get_queryset(self):

        queryset = Article.objects.filter(active=True)

        product_id = self.request.GET.get('product_id')

        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset