from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} , {self.year}"