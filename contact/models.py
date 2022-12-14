from django.db import models

# Create your models here.
class Contact(models.Model):
    full_name = models.CharField(max_length = 45)
    relationship = models.CharField(max_length= 45)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length= 20)
    address = models.CharField(max_length = 45)

    def __str__(self):
        return self.full_name + self.relationship