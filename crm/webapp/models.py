from django.db import models

class Client(models.Model):

    creation_date = models.DateTimeField(auto_now_add=True)
    
    first_name = models.CharField(max_length=50)
    
    last_name = models.CharField(max_length=50)
    
    email = models.CharField(max_length=100)
    
    phone_number = models.CharField(max_length=20)
    
    address = models.CharField(max_length=200)
    
    city = models.CharField(max_length=100)
    
    province = models.CharField(max_length=100)
    
    country = models.CharField(max_length= 100)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
