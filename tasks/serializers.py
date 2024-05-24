from rest_framework import serializers

from tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('todo','done','do_date', 'created','modified',)
        read_only_fields = ('created, modified', 'done',)
        extra_kwargs = {
            'modified': {'required': False}
        }