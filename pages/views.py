from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from listings.models import Listing
from realtors.models import Realtor

from listings.choices import *

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_publised=True)[:3]

    context = {
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedrooms_choices':Bedrooms_choices,
        'listings': listings
    }
    return render(request,'pages/index.html',context)

def about(request):

    realtors = Realtor.objects.order_by('-hire_date')[:3]

    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors':realtors,
        'mvp_realtors':mvp_realtors
    }
    return render(request,'pages/about.html',context=context)


