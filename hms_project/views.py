from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from .models import patient
from django.http import JsonResponse
def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def dashboard(request):
    data = patient.objects.all();
    context = {'data': data}
    return render(request, 'dashboard.html', context)

@csrf_exempt
def addpatient(request):
    if request.method == 'POST':
        patname=request.POST.get('patname')
        patemail=request.POST.get('patemail')
        patage=request.POST.get('patage')
        patdisease=request.POST.get('patdisease')

        obj1=patient(patname=patname,patemail=patemail,patage=patage,patdisease=patdisease)
        obj1.save()

    #fetch the student data to be displayed
    data = patient.objects.all();
    context = {'data':data}
    return render(request, 'dashboard.html', context)


def editpatient(request,id):
  data = patient.objects.get(id=id);
  context = {'data': data}
  return render(request, 'updatepatient.html', context)

def updatepatient(request,id):
  if request.method == 'POST':
    patname = request.POST.get('patname')
    patemail = request.POST.get('patemail')
    patage = request.POST.get('patage')
    patdisease = request.POST.get('patdisease')

    #modify the student details based on the student id given
    editpatient = patient.objects.get(id=id)#here  fetch the student to be changed

    #i make changes based on what came from the database
    editpatient.patname= patname
    editpatient.patemail= patemail
    editpatient.patage= patage
    editpatient.patdisease= patdisease
    #here i am saving the changes
    editpatient.save()

  #here i want to display the new changes in my html table so i fetchh them from my database table
  thedata = patient.objects.all()
  #here i create a dictionary to hold the fetched info
  context = {'data': thedata}
  #here i now pass the ftched info back to my dashoard
  return redirect('/dashboard')

def deletepatient(request,id):
  deletepatient = patient.objects.get(id=id)
  deletepatient.delete()
  return redirect('/dashboard')

