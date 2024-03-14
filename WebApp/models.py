from django.db import models

# Create your models here.

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add = True) #timestamp ogni volta che viene istanziato 
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    state =  models.CharField(max_length=50)
    zipcode =  models.CharField(max_length=20)

    #rappresentazione leggibile di un oggetto come stringa
    def __str__(self):
        return(f"{self.first_name} {self.last_name}") #Output: first_name last_name (es mario rossi)