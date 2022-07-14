from django.db import models

# Create your models here.
class employees(models.Model):
    firstname= models.CharField(max_length=10)
    lastname =models.CharField(max_length=10)
    emp_id= models.IntegerField()
    
    def _atr_(self):
        return self.firstname     