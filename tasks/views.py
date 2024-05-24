from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from tasks.serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
class TaskViewSet(ModelViewSet,
                                viewsets.GenericViewSet):
    """
    A Model view for CRUD actions in tasks.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Get the queryset of tasks for the authenticated user.
        """
        return self.request.user.user_task.all()
    
    @action(detail=True, methods=['post'], url_path='update-status')
    def done_task(self, request, pk=None):
        """
        Toggle the status of a task between done and undone.

        ## Use
        - Make a empty post to this endpoint and it will change the status of the task and retrive the data.
        """
        task = self.get_object()
        task.done = not task.done
        task.save(update_fields=['done'])
        return Response({'id': task.id, 'done': task.done})