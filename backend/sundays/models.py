from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

class Class(models.Model):
    grade = models.DecimalField(max_digits=5, decimal_places=2)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
class AssignmentType(models.Model):
    name = models.CharField(max_length=255)
    weight = models.PositiveSmallIntegerField()
    klass = models.ForeignKey(Class, on_delete=models.CASCADE)
    number_of_assignments = models.PositiveSmallIntegerField()

class Assignment(models.Model):
    grade = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    due_date = models.DateTimeField()
    assignmentType = models.ForeignKey(AssignmentType, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ass_number = models.PositiveSmallIntegerField(default=0)