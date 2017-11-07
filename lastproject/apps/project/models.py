from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from django.db.models import F
from datetime import date
from datetime import datetime
from ..logreg.models import User

class UserManager(models.Manager):

    def GetCurrentUser(self, request):
        print "func GetCurrentUser"
        print (request.session['id'])
        try:
            usrReturn = User.objects.get(id=request.session['id'])
            print "test!! ",User.objects.get(id=request.session['id']).name
            return usrReturn
        except Exception as e:
            print '%s (%s)' % (e.message, type(e))
            return e

    def itemadded(self,data,id):
        error = []
        if len(data['item']) < 3:
            error.append("Item field must be more than 3 characters and cannot be blank!")
        if not error:
            try:
                currentUser = User.objects.get(id=id)
                print 1
                Items.objects.create(user=currentUser,item=data['item'])
                print 2
                return True
            except:
                pass
        else:
            return (False,error)

    def deleteList(self,id):
        print "in delete function - Models"
        objDelete = Items.objects.get(id=id)
        objDelete.delete()
        return True

    def removeList(self,request,id):
        print "in remove function - Models"
        currentUser = self.GetCurrentUser(request)
        item = Items.objects.get(id=id)
        addedwish = AddedWish.objects.get(item=item,name=currentUser.name)
        objDelete = addedwish
        objDelete.delete()
        return True

    def addWish(self,request,id):
        addwish = Items.objects.get(id=id)
        currentUser = self.GetCurrentUser(request)
        print "In addList func - Models, User: ", addwish.user.name
        AddedWish.objects.create(item=addwish,name=currentUser.name)
        return True

class Items(models.Model):
    user = models.ForeignKey(User,related_name="the_user")
    item = models.CharField(max_length=40)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = UserManager()

class AddedWish(models.Model):
    item = models.ForeignKey(Items,related_name="the_item")
    name = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
