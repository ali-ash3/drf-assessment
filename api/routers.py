from .views import AuthorViewSet, BookViewSet, GenreViewSet
from rest_framework import routers


router = routers.DefaultRouter()

router.register('authors', AuthorViewSet)
router.register('genres', GenreViewSet)
router.register('books', BookViewSet)

