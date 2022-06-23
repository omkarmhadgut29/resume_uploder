from django.db import models

# Create your models here.

states_list = ((
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune'),
    ('Bangalore', 'Bangalore'),
))

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField()
    state = models.CharField(max_length=50, choices=states_list)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    pimage = models.ImageField(upload_to="pimage", blank=True)
    docs = models.FileField(upload_to="docs", blank=True)

    def __str__(self) -> str:
        return self.name
