from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    employee_id = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    age = models.CharField(max_length=15)
    position = models.CharField(max_length=25)
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.name