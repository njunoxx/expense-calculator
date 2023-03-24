from django.db import models

# Create your models here.
class Person(models.Model):
    person = models.CharField(max_length=120)
    email = models.EmailField(max_length=120)
    address = models.CharField(max_length=120)
    contact = models.CharField(max_length=120) 

    def __str__(self):
        return self.person
    
    class Meta:
        db_table = 'app_person'


class Expense(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    net_income = models.FloatField(default=0)
    net_expense = models.FloatField(default=0)
    total_balance = models.FloatField(default=0)
    date = models.DateField()

    def __str__(self):
        return str(self.person)
    
    class Meta:
        db_table = 'app_expense'