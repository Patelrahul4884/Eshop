from django.db import models
from django.core.validators import MinLengthValidator

class Customer(models.Model):
    first_name=models.CharField(max_length=50,validators=[MinLengthValidator(2,'First name must be greater than 1 character')])
    last_name=models.CharField(max_length=50,validators=[MinLengthValidator(2,'last name must be greater than 1 character')])
    phone=models.CharField(max_length=10)
    email=models.EmailField()
    password=models.CharField(max_length=500)

    def register(self):
        self.save()
    
    def isExist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
            
    def __str__(self):
        return self.first_name
