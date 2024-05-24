from django.db import models

# Create your models here.

class Task(models.Model):
    '''API TASK MODEL '''
    user        = models.ForeignKey('users.NiceUser', on_delete=models.CASCADE, related_name='user_task')
    todo        = models.TextField(blank=False, null=False)
    done        = models.BooleanField(default=False)
    do_date     = models.DateTimeField(null=True, blank=True)
    created     = models.DateTimeField(editable=False, auto_now_add=True)
    modified    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.user.email} - {self.created}'