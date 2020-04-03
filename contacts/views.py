from django.shortcuts import render,redirect
# Create your views here.
from django.contrib import messages
from contacts.models import Contact

def contact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.message = request.POST['message']
        contact.user_id = request.POST['user_id']
        contact.listing = request.POST['listing']
        contact.listing_id = request.POST['listing_id']
        realtor_email = request.POST['realtor_email']
        contact.save()
        messages.success(request,'Your request has been successful')
        return redirect('/listings/'+ str(contact.listing_id))

