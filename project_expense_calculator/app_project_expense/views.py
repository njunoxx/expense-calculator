from django.shortcuts import render, redirect
from .models import Expense, Person
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views import View


@login_required(login_url='login')
def index(request):
    per = Person.objects.all()
    context = {"data": per}
    return render(request, 'person/index.html', context)

@login_required(login_url='login')
def person_index(request):
    per = Person.objects.all()
    context = {"data": per}
    return render(request, 'person/person_index.html', context)

@login_required(login_url='login')
def per_delete(request, id):
    data = Person.objects.filter(id=id)
    data.delete()
    messages.success(request, "Data deleted successfully!")
    return redirect('index')

@login_required(login_url='login')
def per_edit(request, id):
    data = Person.objects.get(id=id)
    context = {"data" : data}
    return render(request, 'person/edit_profile.html', context)

@login_required(login_url='login')
def person_card(request, id):
    per = Person.objects.get(id=id)
    context={"data":per}
    return render(request, 'person/person_card.html', context)

@login_required(login_url='login')
def per_profile(request, id):
    data1 = Person.objects.get(id=id)
    data= Person.objects.all()
    context={"data":data, "data1":data1}
    return render(request, 'person/person_profile.html', context)

class UserAdd(View):
    def get(self, request):
        return render(request, 'person/person_add.html')
    
    def post(self, request):
        person = request.POST.get('person')
        email = request.POST.get('email')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        try:
            if Person.objects.filter(person=person).exists():
                messages.error(request, "Sorry User has been already registered in the system. Please Try with new one")
                return redirect('person-add')
            else:
                per = Person()
                per.person = person
                per.email = email
                per.address = address
                per.contact = contact
                per.save()
                messages.success(request, "User has been added successfully!")
                return redirect('index')
        except:
            messages.error(request, "OOPS!!! Something went wrong. Please try again.")
            return redirect('index')


# View for Expense
@login_required(login_url='login')
def expense_index(request):
    exp = Expense.objects.all()
    context = {"data":exp}
    return render(request, 'expense/expense_index.html', context)

@login_required(login_url='login')
def expense_card(request, person):
    exp = Expense.objects.filter(person__person =person)
    context={"data":exp}
    return render(request, 'expense/expense_card.html', context)

@login_required(login_url='login')
def per_update(request):
    if request.method == "POST":
        user = Person.objects.get(id=request.POST.get('id'))
        user.email = request.POST.get('email')
        user.address = request.POST.get('address')
        user.contact = request.POST.get('contact')
        user.save()
        messages.success(request, "Profile edited successfully!")
        return redirect('index')

@login_required(login_url='login')
def expense_delete(request, id):
    exp = Expense.objects.get(id=id)
    exp.delete()
    messages.success(request, "User Deleted successfully!!")
    return redirect('exp-index')

@login_required(login_url='login')
def exp_edit(request, id):
    data = Expense.objects.get(id=id)
    context = {"data": data}
    return render(request, 'expense/expense_edit.html', context)   
     
@login_required(login_url='login')
def exp_update(request):
    exp = Expense.objects.get(id=request.POST.get('id'))
    net_income1 = request.POST.get('net_income')
    net_expense1 = request.POST.get('net_expense')
    net_income = float(net_income1)
    net_expense = float(net_expense1)
    exp.total_balance = net_income - net_expense
    exp.net_income = net_income1
    exp.net_expense = net_expense1
    exp.date = request.POST.get('date')
    if exp.total_balance < 0 :
        exp.save()
        messages.warning(request, "Your Expenses for this "+ exp.date +" is higher than your Income!!", )
        return redirect('exp-index')
    else:
        exp.save()
        messages.success(request, "Expense info updated successfully!")
        return redirect('exp-index')
 
class ExpenseAdd(View):
    def get(self, request):
        exp = Person.objects.all()
        context = {"data":exp}
        return render(request, 'expense/expense_Add.html', context)
    
  
    def post(self, request):
        income1 = request.POST.get('net_income')
        expense1 = request.POST.get('net_expense')
        income = float(income1)
        expense = float(expense1)
        balance = income - expense
        
        user = Person.objects.get(id = request.POST.get('person'))
        exp = Expense()
        exp.person = user
        exp.net_income = request.POST.get('net_income')
        exp.net_expense = request.POST.get('net_expense')
        exp.date = request.POST.get('date')
        exp.total_balance = balance
        if balance < 0:
            exp.save()
            messages.warning(request, "User has more Expenses than Incomes on the entered date")
            return redirect('exp-index')
        else:
            exp.save()
            messages.success(request, "Expense Details have been saved successfully!!")
            return redirect('exp-index')
        
        