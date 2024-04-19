from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length = 255)
    discrpition = models.TextField()
    devoloper = models.CharField(max_length = 255)
    date_of_issue = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.name