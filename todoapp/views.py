from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions, serializers
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import TodoSerializer
from .models import TodoModel
from .permissions import AuthorOrForbidden


class TodoViewSet(ModelViewSet):
    queryset = TodoModel.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated, AuthorOrForbidden]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title']

    def list(self, request, *args, **kwargs):
        self.queryset = TodoModel.objects.filter(user=self.request.user)
        return super(TodoViewSet, self).list(request=request, *args, **kwargs)

    @action(methods=["GET"], detail=False, url_path="is_active")
    def is_active_task(self, request):
        return Response("some additional endpoint", 200)
