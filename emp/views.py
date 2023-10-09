from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from datetime import datetime
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request,'emp/index.html')
def add(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        phone=int(request.POST['phone'])

        new_emp=Employee(first_name=first_name,last_name=last_name,bonus=bonus,salary=salary,hire_date=datetime.now(),dept_id=dept,role_id=role)
        new_emp.save()

        return HttpResponse("Employee successfully added")
    elif(request.method=="GET"):
        return render(request,'emp/add.html')
    else:
        # return HttpResponse("erro")
        print('get')
    
def all(request):
    print(Employee.objects.all())
    return render(request,'emp/all.html',{
        'emps':Employee.objects.all()
    })
def remove(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("Employee removed successfully")
        except:
            return HttpResponse("Please enter a valid emp id")
    return render(request,'emp/remove.html',{
        'emps':Employee.objects.all()
    })
def filter(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
        if dept:
            empa=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        
        return render(request,'emp/all.html',{
            'emps':emps
        })
    elif request.method=="GET":
        return render(request,'emp/filter.html')
    else:
        return HttpResponse("AN Exception occured")
        
