from django.shortcuts import render,redirect
from django.http import HttpResponse
from organizer.models import Organizer
from django.contrib.auth.models import User
from customer.models import Booking
from event.models import Event
from customer.models import Booking
# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        data = {}
        user_id = request.user.id
        get_event = Event.objects.filter(uid=user_id)
        get_bookings = Booking.objects.filter(eid__in=get_event)
        data['customers'] = get_bookings

        return render(request, 'organizer/dashboard.html', context=data)
    else:
        return redirect("/")


def add_organizer(request):
   organizer = Organizer.objects.filter(uid=request.user.id)
   if not organizer:
        if request.method=="POST":
            organizer_name = request.POST['organizer_name']
            organizer_description = request.POST['organizer_description']
            organizer_location = request.POST['organizer_location']
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            save_organizer = Organizer.objects.create(name=organizer_name, description=organizer_description, location=organizer_location, uid=user)
            save_organizer.save()
   else:
       return render(request, "organizer/already.html")

   return render(request, "organizer/add_organizer.html")

def delete_booking(request, id):
    booking = Booking.objects.get(id=id)
    booking.delete()
    return redirect("/organizer/dashboard")
