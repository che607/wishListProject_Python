from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import User, Items, AddedWish
from datetime import datetime, date, timedelta

def wishlist(request):
    currentUser = User.objects.GetCurrentUser(request)
    items = Items.objects.all()
    addedwishes = AddedWish.objects.all()
    myitemsarr = []
    otheritemsarr = []
    for item in items:
        if currentUser.name == item.user.name:
            myitemsarr.append(item)
        else:
            otheritemsarr.append(item)
    for addedwish in addedwishes:
        print "name ",addedwish.item.user.name
        if addedwish.name == currentUser.name:
            idx = 0
            while idx < len(otheritemsarr):
            #print otheritemsarr[idx].quote
                if addedwish.item == otheritemsarr[idx]:
                    print 1
                    myitemsarr.append(addedwish.item)
                    del otheritemsarr[idx]
                    idx += 1
                else:
                    print 6
                    idx +=1
    context = {
    "currentUser": currentUser,
    "myitemsarr": myitemsarr,
    "otheritemsarr": otheritemsarr
    }
    return render(request, 'project/wishlist.html', context)

def logout(request):
    return render(request, 'logreg/index.html')

def additem(request):
    currentUser = User.objects.GetCurrentUser(request)
    context = {
    "currentUser": currentUser,
    }
    return render(request, 'project/additem.html',context)

def itemadded(request,id):
    itemadded = Items.objects.itemadded(request.POST,id)
    if itemadded == True:
        print "True"
        print "user.id ",request.session['id']
        return redirect('project:wishlist')
    else:
        print "else"
        #if itemadded == False:
        for error in itemadded[1]:
            messages.error(request, error)
        return redirect('project:additem')

def delete(reuqest,id):
    delete = Items.objects.deleteList(id)
    return redirect('project:wishlist')

def remove(request,id):
    remove = Items.objects.removeList(request,id)
    return redirect('project:wishlist')

def iteminfo(request,id):
    item = Items.objects.get(id=id)
    context = {
    "item": item,
    }
    return render(request, 'project/iteminfo.html',context)

def add2wish(request,id):
    addwish = AddedWish.objects.addWish(request,id)
    return redirect('project:wishlist')
