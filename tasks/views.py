from rest_framework import permissions, viewsets
from rest_framework.request import Request  # Import Request for type hinting

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): # ignore
        if hasattr(self, 'request') and isinstance(self.request, Request):
            status = self.request.query_params.get('status')
            queryset = Task.objects.filter(user=self.request.user)
            if status:
                queryset = queryset.filter(status=status)
            return queryset
        else:
            print("Request object is not available in get_queryset")
            return Task.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
