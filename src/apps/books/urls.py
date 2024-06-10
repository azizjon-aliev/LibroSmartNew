from rest_framework import routers
from .views import CategoryAPIView, AuthorAPIView, BookAPIView

router = routers.DefaultRouter()
router.register(r'categories', CategoryAPIView, basename='category')
router.register(r'authors', AuthorAPIView, basename='author')
router.register(r'books', BookAPIView, basename='book')

urlpatterns = router.urls
