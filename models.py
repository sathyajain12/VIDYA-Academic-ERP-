from django.db import models

class Campus(models.Model):
    code = models.CharField(max_length=3, unique=True)  # PSN, ATP, BRN, NDG
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.code

class Department(models.Model):
    name = models.CharField(max_length=50)
    campuses = models.ManyToManyField(Campus)  # e.g., Management Studies in BRN + ATP

    def __str__(self):
        return self.name

class Program(models.Model):
    code = models.CharField(max_length=10, unique=True)  # e.g., MBA
    name = models.CharField(max_length=50)
    campuses = models.ManyToManyField(Campus)  # e.g., MBA in BRN + ATP

    def __str__(self):
        return self.code