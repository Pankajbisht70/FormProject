from django.shortcuts import render
from django.http import HttpResponse
from.models import *
from.forms import *


def personal_view(request):
    form = Personal_form()
    if request.method == 'POST':
        form = Personal_form('POST')
        if form.is_valid():
            form.save(commit=True)
            print("DATA ADDED SUCCESSFULLY")
            request.session[pform] = form
    return render(request,'SessionApp/personal.html',{'form':form})

def academic_view(request):
    form = Academic_form()
    if request.method == 'POST':
        form = Academic_form('POST')
        if form.is_valid():
            form.save(commit=True)
            print("DATA ADDED SUCCESSFULLY")
            request.session[aform] = form
    return render(request, 'SessionApp/academic.html', {'form': form})

def experience_view(request):
    number = request.GET["number"]
    response = render(request,'SessionApp/experience.html')
    response.set_cookie("number",number)
    return response

def display(request):

    email = request.GET["email"]
    number = request.COOKIES.get('number')
    name = request.COOKIES.get('name')
    my_dict = {"name":name,"number":number,"email":email}

    return render(request, 'SessionApp/display.html',context=my_dict)

# Create your views here.
