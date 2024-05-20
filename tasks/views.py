from rest_framework.viewsets import ModelViewSet

from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.request.user.user_task.all()