from itertools import accumulate

from django.shortcuts import render,get_object_or_404,redirect
from listings.models import Listing
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from .models import Comment
from listings.choices import *

from datetime import datetime
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_publised=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    list_page = paginator.get_page(page)


    return render(request,'listings/listings.html',{'listings':list_page})


def listing(request,list_id):
    listing = get_object_or_404(Listing,pk=list_id)
    comments = Comment.objects.all().filter(active=True).filter(listing_id=listing.id)
    if request.method == 'POST':
        Comments = Comment()
        if request.POST['name'] and request.POST['email'] and request.POST['body']:
            Comments.name = request.POST['name']
            Comments.email = request.POST['email']
            Comments.body = request.POST['body']
            Comments.listing_id = listing.id
            Comments.pub_date = datetime.now()
            Comments.user = request.user
            Comments.active = False
            Comments.post = listing
            Comments.save()
            messages.info(request, 'Your Comment will show up after re watching')

            return redirect('/listings/' + str(listing.id))
        else:
            return render(request, 'listings/listing.html', context={'listing': listing, 'comments': comments})
    else:
        return render(request, 'listings/listing.html', context={'listing': listing, 'comments': comments, })







def search(request):
    queryset_list = Listing.objects.order_by('-list_date').filter(is_publised=True)

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)


    # city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

    # state

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)


    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__iexact=bedrooms)

    context = {
        'state_choices':state_choices,
        'price_choices':price_choices,
        'bedrooms_choices':Bedrooms_choices,
        'listings':queryset_list,
        'values' : request.GET
    }

    return render(request,'listings/search.html',context)