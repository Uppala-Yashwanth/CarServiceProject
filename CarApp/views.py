from django.shortcuts import render, HttpResponseRedirect
from CarApp.forms import CustomerForm,signupform
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView
from CarApp.models import Customer
from django.contrib.auth.decorators import login_required
# Create your views here.

def car(request):
    #car = car.objects.all()
    return render(request, 'CarApp/car_list.html',)

def Customerview(request):
    form = CustomerForm()
    print('welcome')
    if request.method=='POST':
        form= CustomerForm(request.POST)
        if form.is_valid():
            print('Hello')
        user = form.save()
        return render(request, 'CarApp/thank.html')
    else:
        return render(request, 'CarApp/customer.html',{'form':form})



def thankview(request):
    return render(request, 'CarApp/thank.html')

@login_required
def MechanicView(request):
    return render(request, 'CarApp/home1.html')

class customerlist(ListView):
    model = Customer

class CustomerDetail(DetailView):
    model = Customer
    template_name = 'CarApp/Mechanic.html'

def signupview(request):
    sent = False
    form = signupform()
    if request.method=='POST':
        form = signupform(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            sent = True
            return HttpResponseRedirect('/accounts/login/' ,{'sent':sent})
    else:
        form = signupform()
    return render(request,'CarApp/signup.html',{'form':form ,'sent':sent})

def logout(request):
    request.session.clear()
    return render(request,'CarApp/logout.html')