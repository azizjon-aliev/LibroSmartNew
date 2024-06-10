from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class AbstractSlugModel(models.Model):
    slug = models.SlugField(verbose_name="slug", max_length=255, unique=True)

    class Meta:
        abstract = True


class AbstractTimestampsModel(models.Model):
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    class Meta:
        abstract = True


class AbstractAuditableModel(models.Model):
    created_by = models.ForeignKey(
        to=User,
        verbose_name="Кто создал",
        on_delete=models.SET_NULL,
        related_name="%(class)s_created_by",
        blank=True,
        null=True,
    )
    updated_by = models.ForeignKey(
        to=User,
        verbose_name="Кто изменил",
        on_delete=models.SET_NULL,
        related_name="%(class)s_updated_by",
        blank=True,
        null=True,
    )

    class Meta:
        abstract = True
