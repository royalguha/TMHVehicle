from django.shortcuts import render,redirect
from .forms import booking_form,booking_confirm_form
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.auth.decorators import login_required
from .models import profile,role_master,booking
from django.views.generic import UpdateView


# Create your views here.
def index(request):
    if request.method=="POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                messages.error(request,"Invalid Credentials!")
        else:
            messages.error(request,"Invalid Credentials!")

    form = AuthenticationForm()
    return render(request,"login.html",{"loginform":form})

@login_required
def home(request):
    if request.method=="POST":
        form = booking_form(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect("index")
        
    else:
        booking_det=booking.objects.all()
        
    return render(request,"index.html",{"bookingform":booking_form,"booking_det":booking_det,"bookingconfirmform":booking_confirm_form})




class DataUpdateView(UpdateView):
    
    template_name = "update.html"
    model = booking
    fields = "__all__"
    success_url = "/home"
    
def detail(request,**kwargs):
    if request.method=="POST":
        pass
    else:
        details = booking.objects.filter(id=kwargs["pk"])
        return render(request,"detail.html",{"details":details})


def delete(request,**kwargs):
    if request.method == "POST":
        pass
    else:
        item = booking.objects.filter(id=kwargs["pk"])
        item.delete()
        return redirect("/home")