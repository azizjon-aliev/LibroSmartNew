from django.db.models import Q
from .models import Category, Author, Book
from .serializers import (
    CategoryResponseListSerializer,
    CategoryResponseDetailSerializer,
    CategoryUpdateSerializer,
    CategoryCreateSerializer,
    AuthorUpdateSerializer,
    AuthorCreateSerializer,
    AuthorResponseDetailSerializer,
    AuthorResponseListSerializer,
    BookResponseListSerializer,
    BookResponseDetailSerializer,
    BookCreateSerializer,
    BookUpdateSerializer,
)
from ..common.views import BaseAPIView


class CategoryAPIView(BaseAPIView):
    list_serializer = CategoryResponseListSerializer
    detail_serializer = CategoryResponseDetailSerializer
    create_serializer = CategoryCreateSerializer
    update_serializer = CategoryUpdateSerializer

    def get_queryset(self):
        return Category.objects.filter(Q(created_by=self.request.user) | Q(updated_by=self.request.user), parent=None)


class AuthorAPIView(BaseAPIView):
    list_serializer = AuthorResponseListSerializer
    detail_serializer = AuthorResponseDetailSerializer
    create_serializer = AuthorCreateSerializer
    update_serializer = AuthorUpdateSerializer
    lookup_field = "pk"

    def get_queryset(self):
        return Author.objects.filter(Q(created_by=self.request.user) | Q(updated_by=self.request.user))


class BookAPIView(BaseAPIView):
    list_serializer = BookResponseListSerializer
    detail_serializer = BookResponseDetailSerializer
    create_serializer = BookCreateSerializer
    update_serializer = BookUpdateSerializer

    def get_queryset(self):
        return Book.objects.filter(Q(created_by=self.request.user) | Q(updated_by=self.request.user))
