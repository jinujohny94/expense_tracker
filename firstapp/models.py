from django.db import models

# Create your models here.

class Employer(models.Model):
    employer_id=models.IntegerField(primary_key=True)
    employer_name=models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.employer_name

class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    salary=models.IntegerField()
    employer_name=models.ForeignKey(Employer,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
