from django.shortcuts import render, redirect
from event.models import Event
from .models import Event, Organizer, User
def add_event(request):

    if(request.method=="POST"):
        event_name = request.POST['event_name']
        image = request.FILES.get('image')
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        category = request.POST['category']
        event_location = request.POST['event_location']
        event_description = request.POST['event_description']
        price = request.POST['price']
        print(image)
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        save_event = Event.objects.create(name=event_name, image=image, startdate=start_date, enddate=end_date, category=category, eventdescription=event_description, eventlocation=event_location, uid=user, price=price)

        save_event.save()

        return redirect("/event")
    
    return render(request, 'event/add_event.html')

def show_event(request):
    data={}
    user = request.user.id
    my_events=Event.objects.filter(uid=user)
    print(my_events)
    data['events'] = my_events
    return render(request, "event/event_detail.html", context=data)

def delete_event(request, id):
    delete_event = Event.objects.get(id=id)
    delete_event.delete()
    return redirect("/event")

def update_event(request, id):
   data={}
   event = Event.objects.filter(id=id)
   data['event'] = event[0]

   if(request.method=="POST"):
        event_name = request.POST['event_name']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        category = request.POST['category']
        event_location = request.POST['event_location']
        event_description = request.POST['event_description']
        price = request.POST['price']
        event.update(name=event_name, startdate=start_date, enddate=end_date, category=category, eventdescription=event_description, eventlocation=event_location, price=price)


        return redirect("/event")
       
   return render(request, "event/event_update.html", context=data)
    