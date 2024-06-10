from rest_framework import serializers
from src.apps.books.models import Author
from src.apps.common.serializers import UserShortSerializer


class AuthorResponseListSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    def get_books_count(self, obj):
        return obj.books.count()

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            "birth_date",
            "books_count",
            'created_at',
        )


class AuthorResponseDetailSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = Author
        fields = (
            'id',
            'first_name',
            'last_name',
            "birth_date",
            "death_date",
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )


class AuthorCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
            "birth_date",
            "death_date",
            'created_by',
            'updated_by',
        )


class AuthorUpdateSerializer(serializers.ModelSerializer):
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = (
            'first_name',
            'last_name',
            "birth_date",
            "death_date",
            'updated_by',
        )


