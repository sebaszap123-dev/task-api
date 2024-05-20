from django.test import TestCase

from tasks.models import Task
from users.models import NiceUser

# Create your tests here.

class TaskTestCaseManager(TestCase):
    def test_create_task(self):
        user = NiceUser.objects.create_user(email="normal@user.com", password="foo")
        task = Task.objects.create(user=user, todo='Muchas cosas', do_date=None)
        self.assertEqual(user.email, task.user.email)
        self.assertFalse(task.done)
        self.assertIsNone(task.do_date)