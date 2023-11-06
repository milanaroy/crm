from django.db import models


# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=200)
    department=models.CharField(max_length=200)
    salary=models.PositiveIntegerField()
    email=models.EmailField(unique=True)
    age=models.PositiveBigIntegerField()
    contact=models.CharField(null=True,max_length=200)

    def __str__(self) :
        return self.name
