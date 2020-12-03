from django.db import models


class UserTestManager(models.Manager):
    def print_test(self, text):
        print('test')


class UserTest(models.Model):
    """test table(user)"""

    name = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    age = models.IntegerField()

    objects = UserTestManager()


user = UserTest.objects

