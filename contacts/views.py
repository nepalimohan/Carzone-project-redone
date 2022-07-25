from django.shortcuts import redirect, render
from  .models import Contact
from django.contrib import messages

# Create your views here.
def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_needs = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        
        contact = Contact(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name, last_name=last_name,
                          customer_needs=customer_needs, city=city, state=state, email=email, phone=phone, message=message)
        contact.save()
        messages.success(request, "Your messgae has been received. We will get back to you shortly!!!")
        return redirect('/cars/'+car_id)