from django.db import models

# Create your models here.
class UsersPuma(models.Model):
    name = models.CharField(max_length=100)
    position = models.TextField()
    office = models.TextField()
    age = models.IntegerField()
    start_date = models.DateField(null=True)
    salary = models.IntegerField()

    def serialize(self):
        return {
            "name": self.name,
            "position": self.position,
            "office": self.office,
        }