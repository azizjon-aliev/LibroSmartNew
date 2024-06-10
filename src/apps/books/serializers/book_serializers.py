from rest_framework import serializers
from src.apps.books.models import Book
from src.apps.books.serializers.author_serializers import AuthorResponseListSerializer
from src.apps.common.serializers import UserShortSerializer


class BookResponseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'slug',
            'created_at',
        )


class BookResponseDetailSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()
    authors = AuthorResponseListSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            "image",
            'title',
            'slug',
            'description',
            'publication_date',
            "is_published",
            'price',
            'authors',
            'category',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )


class BookCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Book
        fields = (
            "image",
            'title',
            'slug',
            'description',
            'publication_date',
            "is_published",
            'price',
            'authors',
            'category',
            'created_by',
            'updated_by',
        )


class BookUpdateSerializer(serializers.ModelSerializer):
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Book
        fields = (
            'title',
            'slug',
            'description',
            'publication_date',
            "is_published",
            'price',
            'authors',
            'category',
            'updated_by',
        )
