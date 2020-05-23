from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse,Http404
from django.contrib.auth import authenticate, login
import random
from ccp.models import Customer
from ccp.models import historydata
import datetime

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
#from ccp.forms import SignUpForm
chances=0
def first(request):
    return render(request,'ccp/first.html',{})
def home(request):
     return render(request,'ccp/home_new.html',{})
def home1(request):
    return HttpResponseRedirect(
               reverse(NAME_OF_PROFILE_VIEW, 
                       args=[request.user.username]))
def request1(request):
    send_mail('hello from Divya','hell this is your mesaage','jainatishay71@gmail.com',['jainatishay71@gmail.com','bodapudidivya@gmail.com'],fail_silently=False)
    return HttpResponse('EMAIL SENT')	
def output(request,customer_id):
       
       return HttpResponse("<h1 > customer name is "+str(customer_id)+"</h1>")
def login(request):
    if request.method=='POST':
     name=request.POST['Email']
     password=request.POST['Password']
     try:
        ans=Customer.objects.get(email=name)
     except:
        ans=None
     if  ans is not None:
       if ans.password==password:
          
          context={
	  'name':ans.name,
	  'email':ans.email,
	  'pan':ans.pan,}
          return render(request,'ccp/yourhome.html',context)
       else:
           context= {
	     'msg':'give correct details',
	   }
           return render(request,'ccp/index.html',context)
     else:
        context={'msg':'no such registered user',}
        return render(request,'ccp/index.html',context)	
    else:
    
     return render(request,'ccp/index.html',{})
    
def display(request):
      customer_list=Customer.objects.all()
      html=''
      for i in customer_list:
      
       url='contact/'+i.name
       html+='<a href=" ' +url+ '">'+url+'</a><br>'
      return HttpResponse(html)
def display1(request,id):
    ans=Customer.objects.get(name=id)
    context={
    'name':ans.name,
    'email':ans.email,
    'number':ans.phonenumber,
    'phno':ans.phonenumber,
    'pan':ans.pan,
    'card':ans.cardno,
    'cardtype':ans.cardtype,
    'occup':ans.occup,
    'address':ans.address,
    'bank':ans.bank,
    'income':ans.income,
    }
    return render(request,'ccp/display.html',context)
def yourhome(request,id):
    ans=Customer.objects.get(name=id)
    context={
    'name':ans.name,
    'email':ans.email,
    'number':ans.phonenumber,
    'pan':ans.pan,
    }
    return render(request,'ccp/yourhome.html',context)
def cprofile(request): 
        customer_list=Customer.objects.all()
        context={'customer_list':customer_list,}
        return render(request,'ccp/profile.html',context)
    
    
def errorview(request,id):
     
     try:
       customer=Customer.objects.get(name=id)
     except Customer.DoesNotExist or customer.DoesNotExist:
       raise   Http404(" * give correct login details")
     url='contact/'+i.name
     return render(request,url,customer)

def history1(request,id):
    #return  HttpResponse("hello"+id)
     try:
      translist=historydata.objects.filter(sender=id)
      trans=historydata.objects.filter(receiver=id)
     except:
      translist=None
     if translist is not None and trans is not None:
      url='ccp/history1.html'
      context={'list':translist,
              'list1':trans,
               'name':id,
             }
      return render(request,'ccp/history1.html',context)
     else:
       return HttpResponse("NO HISTORY YET")

def payment(request,id):
    url='ccp/paying.html'
    # global chances
    k=Customer.objects.get(name=id)
    if request.method=='POST':
        rec=request.POST['name']
        amt=request.POST['Amount']
        pin=request.POST['password']
        try:
          ans=Customer.objects.get(email=rec)
        except:
          ans=None
        if ans is None:
           context={'name':id,'msg':'No such Registered Receiver',}
           return render(request,url,context)
        else:  
             if  pin!=k.password:
                context={'name':id,'msg':'Invalid Password',}
                return render(request,url,context)
             if(k.cardtype=='Rupay'):
                if int(amt)>(20000):
                    context={'name':id,'msg':'The limit of Rupay is 20000! Kindly check the requested amount:)',}
                    return render(request,url,context)
                else:
                 chances=0
                 k.save()
                 ans.save()
                 context={'name':id,'msg':'Money Sent',}
                 now = datetime.datetime.now()
                 t=historydata()
                 t.sender=id
                 t.receiver=ans.name
                 t.amountsent=amt
                 t.date=now.day
                 t.month=now.month
                 t.year=now.year
                 t.hrs=now.hour
                 t.minutes=now.minute
                 t.seconds=now.second
                 t.save()
                 return render(request,url,context)

             elif(k.cardtype=='Visa'):
                if int(amt)>(40000):
                    context={'name':id,'msg':'The limit of Visa is 40000! Kindly check the requested amount:)',}
                    return render(request,url,context)
                else:
                 chances=0
                 k.save()
                 ans.save()
                 context={'name':id,'msg':'Money Sent',}
                 now = datetime.datetime.now()
                 t=historydata()
                 t.sender=id
                 t.receiver=ans.name
                 t.amountsent=amt
                 t.date=now.day
                 t.month=now.month
                 t.year=now.year
                 t.hrs=now.hour
                 t.minutes=now.minute
                 t.seconds=now.second
                 t.save()
                 return render(request,url,context)

             elif(k.cardtype=='Platinum'):
                if int(amt)>(60000):
                    context={'name':id,'msg':'The limit of Platinum is 60000! Kindly check the requested amount:)',}
                    return render(request,url,context)
                else:
                   chances=0
                   k.save()
                   ans.save()
                   context={'name':id,'msg':'Money Sent',}
                   now = datetime.datetime.now()
                   t=historydata()
                   t.sender=id
                   t.receiver=ans.name
                   t.amountsent=amt
                   t.date=now.day
                   t.month=now.month
                   t.year=now.year
                   t.hrs=now.hour
                   t.minutes=now.minute
                   t.seconds=now.second
                   t.save()
                   return render(request,url,context)      
    else:
        url='ccp/paying.html'
        context={'name':id,}
        return render(request,url,context)    
  
def register(request):
     if request.method=='POST':
        name=request.POST['name']
        lname=request.POST['lname']
        email=request.POST['Email Address']
        cardtype=request.POST['cardtype']
        income=request.POST['income']
        number=request.POST['PhoneNumber']
        password=request.POST['Set A Password']
        pan1=request.POST['pan1']
        name=name+" "+lname
        occp=request.POST['occp']
        stno=request.POST['stno']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        address=stno+city+state+country+" "+pincode

        try:

            ans=Customer.objects.get(name=name)
        except:
            ans=None
        if ans is None:
           obj=Customer()
           iden = random.randint(10000000000000000,99999999999999999);
           obj.email=email
           obj.name=name
           obj.password=password

           obj.phonenumber=number
           obj.pan=pan1
           obj.cardno=str(iden)
           obj.address=address
           obj.cardtype=cardtype
           obj.income=income
           obj.save()
           context={'name':name}
        #template = loader.get_template('ccp/profile.html')
        #return HttpResponse("<h1 > customer name is "+"hii"+"</h1>")
        #return HttpResponse(template.render(context, request))
           return render(request,'ccp/profile1.html',context)
        else:
          context={
	      'msg':'user already registered',
	      }
          return render(request,'ccp/signup1.html',context)    
     elif request.method=='GET':
       
        return render(request,'ccp/signup1.html',{})    

def registerf(request):
     if request.method=='POST':
        name=request.POST['name']
        lname=request.POST['lname']
        email=request.POST['Email Address']
        cardtype=request.POST['cardtype']
        income=request.POST['income']
        pnumber=request.POST['PhoneNumber']
        bank=request.POST['bank']
        password=request.POST['Set A Password']
        pan1=request.POST['pan1']
        name=name+" "+lname
        occp=request.POST['occp']
        stno=request.POST['stno']
        city=request.POST['city']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        address=stno+city+state+country+" "+pincode

        try:
            ans=Customer.objects.get(email=email)
        except:
            ans=None
        if ans is None:
           obj=Customer()
           iden = random.randint(1000000000000000,9999999999999999);
           obj.name=name
           obj.occup=occp
           obj.cardtype=cardtype
           obj.address=address
           obj.phonenumber=pnumber
           obj.income=income
           obj.bank=bank
           obj.email=email
           obj.password=password
           obj.cardno=str(iden)
           obj.pan=pan1
           obj.save()
           context={'name':name}
           return render(request,'ccp/first.html',context)
        else:
          context={'msg':'User already registered with this Mail-Id',}
          return render(request,'ccp/form.html',context)    

     elif request.method=='GET':
       return render(request,'ccp/form.html',{}) 

def logout(request):
    return render(request,'ccp/first.html',{})     

def dynasty():
  return render(request,'ccp/signup1.html',{})     
# def mylogin(request):
    # username = request.POST['username']
    # password = request.POST['password']
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
        # login(request, user)
        # # Redirect to a success page.
         
    # else:
        # # Return an 'invalid login' error message.
        