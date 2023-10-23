from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    location = models.ForeignKey(Location, on_delete=models.RESTRICT)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


