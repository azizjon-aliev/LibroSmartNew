from django.contrib import admin
from django.utils.html import format_html

from .models import Category, Author, Book


class BaseModelAdmin(admin.ModelAdmin):
    """ Base model admin """
    empty_value_display = '-пусто-'
    readonly_fields = ['created_at', 'updated_at', 'created_by', 'updated_by']

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(BaseModelAdmin):
    """ Category admin
    """
    list_display = ('name', 'parent', "created_at",)
    search_fields = ('name',)
    list_filter = ('parent',)
    autocomplete_fields = ('parent',)
    prepopulated_fields = {'slug': ('name',)}

    fieldsets = (
        (
            "Общая информация",
            {
                'fields': (
                    'name',
                    "slug",
                    'parent',
                )
            }
        ),
        (

            "Даты создания и обновления",
            {
                'fields': (
                    'created_at',
                    'updated_at',
                ),
                'classes': ('collapse',)
            }
        ),
        (
            "Кто создал и кто обновил",
            {
                'fields': (
                    'created_by',
                    'updated_by',
                ),
                'classes': ('collapse',)
            }
        )
    )


@admin.register(Author)
class AuthorAdmin(BaseModelAdmin):
    """ Author admin
    """
    list_display = ('first_name', 'last_name', 'birth_date', 'death_date',)
    search_fields = ('first_name', 'last_name',)
    list_filter = ('birth_date', 'death_date',)
    date_hierarchy = 'birth_date'

    fieldsets = (
        (
            "Общая информация",
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'birth_date',
                    'death_date',
                )
            },
        ),
        (
            "Даты создания и обновления",
            {
                'fields': (
                    'created_at',
                    'updated_at',
                ),
                'classes': ('collapse',)
            }
        ),
        (
            "Кто создал и кто обновил",
            {
                'fields': (
                    'created_by',
                    'updated_by',
                ),
                'classes': ('collapse',)
            }
        )
    )


@admin.register(Book)
class BookAdmin(BaseModelAdmin):
    """ Book admin
    """
    list_display = ('title', 'image_preview', 'price', 'category', 'is_published',)
    search_fields = ('title', 'description',)
    list_filter = ('category', 'authors', 'is_published',)
    autocomplete_fields = ('category', 'authors',)
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (
            "Изображение",
            {
                'fields': (
                    'image',
                    'image_preview',
                )
            }
        ),
        (

            "Общая информация",
            {
                'fields': (
                    'title',
                    "slug",
                    'description',
                    'price',
                    'category',
                    'authors',
                )
            },
        ),
        (
            "Публикация",
            {
                'fields': (
                    'is_published',
                    'publication_date',
                ),
            }
        ),
        (
            "Даты создания и обновления",
            {
                'fields': (
                    'created_at',
                    'updated_at',
                ),
                'classes': ('collapse',)
            }
        ),
        (
            "Кто создал и кто обновил",
            {
                'fields': (
                    'created_by',
                    'updated_by',
                ),
                'classes': ('collapse',)
            }
        )
    )

    def get_readonly_fields(self, request, obj=None):
        return self.readonly_fields + ['image_preview']

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="{100}" height={100} />')

    image_preview.short_description = 'Превью изображения'
    image_preview.allow_tags = True
    image_preview.empty_value_display = '-пусто-'
