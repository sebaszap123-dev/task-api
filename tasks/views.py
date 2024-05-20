from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer
@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, World!'})

class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    # permission_classes = [IsAuthenticated]
    def get_queryset(self):
        print(self.request.user.user_task.all())
        return Task.objects.all()