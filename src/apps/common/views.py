from http import HTTPMethod
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response


class Action:
    LIST = "list"
    CREATE = "create"
    RETRIEVE = "retrieve"
    UPDATE = "update"
    PARTIAL_UPDATE = "partial_update"
    DESTROY = "destroy"


class BaseAPIView(viewsets.ModelViewSet):
    """Base API view with operations CRUD for model exchange rate"""

    list_serializer = None
    detail_serializer = None
    create_serializer = None
    update_serializer = None

    http_method_names = [
        HTTPMethod.GET.lower(),
        HTTPMethod.POST.lower(),
        HTTPMethod.PATCH.lower(),
        HTTPMethod.DELETE.lower(),
        HTTPMethod.OPTIONS.lower(),
    ]

    lookup_field = 'slug'
    permission_classes = (IsAuthenticated,)

    def __init__(self, *args, **kwargs):
        if self.list_serializer is None:
            raise ValueError("list_serializer is required")
        if self.detail_serializer is None:
            raise ValueError("detail_serializer is required")
        if self.create_serializer is None:
            raise ValueError("create_serializer is required")
        if self.update_serializer is None:
            raise ValueError("update_serializer is required")
        super().__init__(*args, **kwargs)

    def get_serializer_class(self):
        if self.action == Action.LIST:
            return self.list_serializer
        elif self.action == Action.CREATE:
            return self.create_serializer
        elif self.action in [Action.UPDATE, Action.PARTIAL_UPDATE]:
            return self.update_serializer
        elif self.action == Action.RETRIEVE:
            return self.detail_serializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        return {"request": self.request}

    def list(self, request: Request, *args, **kwargs) -> Response:
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer_class()(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        instance = self.get_object()
        return Response(self.get_serializer_class()(instance).data)

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.create_serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(
            self.detail_serializer(instance, context={"request": request}).data,
            status=status.HTTP_201_CREATED,
        )

    def update(self, request: Request, *args, **kwargs) -> Response:
        partial = kwargs.pop("partial", False)
        instance = self.get_object()

        serializer = self.update_serializer(
            instance, data=request.data, partial=partial,
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}

        return Response(self.detail_serializer(instance).data)
