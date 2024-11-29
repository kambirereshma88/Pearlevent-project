from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from organizer.models import Organizer
from customer.models import Booking
from django.db.models import Q
from event.models import Event


# Create your views here.
# events = Event.objects.none()
def home(request):
   return render(request, "customer/home.html")

def register(request):
   data={}
   is_staff=False
   if(request.method=="POST"):
      uname=request.POST['username']
      upass=request.POST['password']
      ucpass=request.POST['cpassword']
      type=request.POST['type']
      if(type=='organizer'):
         is_staff=True
      if(uname=="" or upass=="" or ucpass==""):
         data['error_msg']="fields cant be empty"
         return render(request,'customer/register.html',context=data)
      elif(upass!=ucpass):
         data['error_msg']="password does not matched"
         return render(request,'customer/register.html',context=data)
      #from django.contrib.auth.models import User
      elif(User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + " is already exist"
         return render(request,'customer/register.html',context=data)
      else:
         user=User.objects.create(username=uname,is_staff=is_staff)
         user.set_password(upass)
         user.save()
         return redirect('/login')
   return render(request,'customer/register.html',context=data)


def customer_login(request):
   data={}
   if(request.method=="POST"):
      uname=request.POST['username']
      upass=request.POST['password']
      if(uname=="" or upass==""):
         data['error_msg']="fields cant be empty"
         return render(request,'customer/login.html',context=data)
      elif(not User.objects.filter(username=uname).exists()):
         data['error_msg']=uname + " is does not exist"
         return render(request,'customer/login.html',context=data)
      else:
         
         user=authenticate(username=uname, password=upass)
         if user is None:
            data['error_msg']="Wrong password"
            return render(request,'customer/login.html',context=data)
         else:
            login(request, user)
            if(user.is_staff==True):
            
               return redirect('/service')
            else:
               return redirect('/')
   return render(request,'customer/login.html')


def customer_logout(request):
   logout(request)
   return redirect("/")


def service(request):
   data={}
   events = Event.objects.all()
   data['events'] = events
   return render(request, "customer/service.html", context=data)

import razorpay
def book_event(request, id):
    data1 = {}
    event = Event.objects.get(id=id)  # Get the actual Event instance
    data1['events'] = event
    total_price = int(event.price * 100)
    data1['total_price'] = total_price  
    print(f"Total Price (in paise): {total_price}") 

    client = razorpay.Client(auth=("rzp_test_XRjX6qJ69ajxxs", "s56837vKNGmoW2BiQkQbC3sH"))
    data = {"amount": total_price, "currency": "INR", "receipt": "order_rcptid_11"}
    payment = client.order.create(data=data)
    data1['payment'] = payment

    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        # Create a Booking instance with the actual Event instance
        save_booking = Booking.objects.create(
            category=event.name,  # If you want to store the event's name as category
            name=full_name,
            email=email,
            address=address,
            phonenumber=phone_number,
            eid=event  # Assign the actual Event instance
        )
        save_booking.save()

        return redirect("/service")

    return render(request, "customer/book_event.html", context=data1)

 

def search_event(request):
    data={}
    if(request.method=="POST"):
      eventlocation = request.POST['eventlocation']
      print(eventlocation)
      get_events = Event.objects.all()
      searched_events = get_events.filter(Q(eventlocation__icontains=eventlocation))
      data['events']=searched_events
      return render(request, "customer/service.html", context=data)  
    return render(request, "customer/service.html", context=data)