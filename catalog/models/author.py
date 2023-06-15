from django.db import models
from django.urls import reverse

class Author(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField(default=0)
    data_of_death = models.DateField('Died', null=True, blank=True)



    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("author_detail", args=[str(self.id)])
    
