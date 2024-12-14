from django.db import models

# Create your models here.
class Course(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    maximum_capacity = models.PositiveIntegerField()
    current_enrolled = models.PositiveIntegerField(default=0)


    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrolled_courses = models.ManyToManyField(Course, blank=True)

    def __str__(self):
        return self.name