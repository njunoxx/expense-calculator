from django.contrib import admin
from .models import Person, Expense
# Register your models here.

class AdminPerson(admin.ModelAdmin):
    list_display=("person", "email", "address", "contact")

class AdminExpense(admin.ModelAdmin):
    list_display=("person", "net_income", "net_expense", "total_balance")

admin.site.register(Person, AdminPerson)
admin.site.register(Expense, AdminExpense)

admin.site.site_header = 'EXC'
admin.site.site_title='EXC'
admin.site.index_title='Admin Panel'