from django.contrib import admin

from tasks.models import Task

# Register your models here.
@admin.register(Task)
class TaskAdminManager(admin.ModelAdmin):
    list_display = ("user", "todo", "done", "do_date", "created", "modified",)
    list_filter = ("user", "todo", "done",)
    readonly_fields = ("created", "modified",)