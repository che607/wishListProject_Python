from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse,redirect
from django.contrib import messages
from .models import User


def index(request):
    return render(request, 'logreg/index.html')

def register(request):
    validation = User.objects.register(request.POST)
    print 1
    print request.POST['dob']
    print validation[0]
    if validation[0] == True:
        request.session['name'] = request.POST['name']
        request.session['id'] = validation[2].id
        print "user id ",request.session['id']
        return redirect('project:wishlist')
    else:
        print ("False")
        for error in validation[1]:
                messages.error(request, error)
        return render(request, 'logreg/index.html')

def login(request):

    logininformation = User.objects.login(request.POST)

    if logininformation[0] == True:
        request.session['id'] = logininformation[2].id
        for success in logininformation[1]:
                messages.success(request, success)
        return redirect('project:wishlist')
    else:
        print ("False")
        for error in logininformation[1]:
                messages.error(request, error)
        return render(request, 'logreg/index.html')
