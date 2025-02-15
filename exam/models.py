from django.db import models

class Developer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=100)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    


