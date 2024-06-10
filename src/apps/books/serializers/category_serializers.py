from rest_framework import serializers

from src.apps.books.models import Category
from src.apps.common.serializers import UserShortSerializer


class CategoryResponseListSerializer(serializers.ModelSerializer):
    children_counts = serializers.SerializerMethodField()

    def get_children_counts(self, obj):
        return obj.children.count()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'children_counts',
            'created_at',
        )


class CategoryResponseDetailSerializer(serializers.ModelSerializer):
    created_by = UserShortSerializer()
    updated_by = UserShortSerializer()

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'slug',
            'created_at',
            'updated_at',
            'created_by',
            'updated_by',
        )


class CategoryCreateSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = (
            'name',
            "parent",
            'created_by',
            'updated_by',
        )


class CategoryUpdateSerializer(serializers.ModelSerializer):
    updated_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = (
            'name',
            "parent",
            'updated_by',
        )
