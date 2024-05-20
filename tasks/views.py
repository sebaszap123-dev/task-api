from rest_framework.viewsets import ModelViewSet

from tasks.serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response 
class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return self.request.user.user_task.all()
    
    def create(self, request, *args, **kwargs):
        # Crear la instancia del serializer sin guardar aún
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Crear la tarea asignando el usuario autenticado
        task = serializer.save(user=request.user)
        return Response(serializer.data, status=201)