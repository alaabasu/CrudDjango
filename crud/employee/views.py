
from enum import member
from pyexpat.errors import messages
from types import MemberDescriptorType
from unittest import loader
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render 
from employee.models import Employee, Vacation
from employee.forms import EmployeeForm 
from .forms import  Vacation, VacationForm
from django.views.decorators.csrf import requires_csrf_token

def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except Exception as e:
                print(e)
                # Handle the exception appropriately (e.g., log the error)
    else:
        form = EmployeeForm()

    return render(request, 'index.html', {'form': form})
           

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():  
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})



def show(request):
    employees = Employee.objects.all()
    return render(request, 'show.html', {'employees': employees})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/show")

def main(request):
    return render(request, 'main.html')




def submit_vacation(request, id):
    if request.method == 'POST':
        formset = VacationForm(request.POST)
        if formset.is_valid():
            formset.save()
            return redirect("/submitted")
    else:
        
        form = VacationForm(initial={'employee_id': id})
    return render(request, 'vecation.html', {'employee_id': id, 'form': form}) 


def submitted(request):
    vacations = Vacation.objects.all()
    return render(request, 'submitted.html', {'vacations': vacations})


    

def search_employees(request):
    search_query = request.GET.get('search', '')
    employees = Employee.objects.filter(ename__icontains=search_query)
    return render(request, 'search.html', {'employees': employees, 'search_query': search_query})


        

def des(request, id):
    vacation = get_object_or_404(Vacation, id=id)
    vacation.delete()  # Call delete() on the vacation instance
    return redirect("/submitted")



def approve_vacation(request, employee_id):
    # Update vacation and available counts in the database
    employee = Employee.objects.get(id=employee_id)
    employee.eApprocedvecation += 1
    employee.enumberofavailable -= 1
    employee.save()

    return JsonResponse({'success': True})

