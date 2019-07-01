from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    login_datetime = models.DateTimeField()

    def __str__(self):
        return 'Id: %s' % self.id

