from django.shortcuts import render
from firstapp.models import Employee,Employer
from . import forms
from firstapp.forms import EmpForm

# Create your views here.
from django.http import HttpResponse
def index(request):
    my_dict={'insert_me' : "HELLLLOOO"}
    return render(request, 'firstapp/index.html',context=my_dict)

def testhtml(request):
    return HttpResponse('<em> Test HTML </em>')

def empDetails(request):
    emp_list=Employee.objects.order_by('name')
    #print(emp_list)
    emp_dict={'emp_records':emp_list}
    return render(request,'firstapp/index.html',context=emp_dict)

def get_user(request):
    form=forms.UserForm()
    if request.method == "POST":
        form=forms.UserForm(request.POST)
        if form.is_valid():
            print("Welcome",form.cleaned_data['user_name'])

    return render(request,'firstapp/form_page.html',context={'userform':form})

def signemp(request):
    form=EmpForm()
    if request.method == 'POST':
        form=EmpForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return empDetails(request)
    else:
        print("Error")
        return render(request,'firstapp/emp.html',{'form':form})        

