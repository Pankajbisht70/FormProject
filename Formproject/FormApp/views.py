from django.shortcuts import render
from .forms import Indiajobsform
from .models import IndiaJobs
# Create your views here.


def welcome(request):
    return render(request,"FormApp/Formindex.html")


def add_form(request):
    form = Indiajobsform()
    if request.method == "POST":
        form = Indiajobsform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Data Added sucessfully !")
        return welcome(request)
    return render(request,'FormApp/Formfill.html',{'form':form})


def view_job(request):
    job_list = IndiaJobs.objects.all()
    return render(request,'FormApp/Formlist.html',{'job_list':job_list})


