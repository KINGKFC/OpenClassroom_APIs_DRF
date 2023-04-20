from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from shop.views import CategoryAPIViewset, ProductAPIViewset, ArticleAPIViewset

from shop.views import CategoryAPIViewset

# On définit le router nécessaire pour les endpoints et on les enrégistre
router = routers.SimpleRouter()
router.register('category', CategoryAPIViewset, basename='category')
router.register('product', ProductAPIViewset, basename='product')
router.register('article', ArticleAPIViewset, basename='article')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
    # path('api/category/', CategoryAPIView.as_view()),
    # path('api/product/', ProductAPIView.as_view())
]
