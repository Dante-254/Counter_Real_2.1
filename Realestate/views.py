from django.shortcuts import render, redirect
from .models import Listing
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import ListingSearchForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def search(request):
    form = ListingSearchForm(request.GET)
    listings = Listing.objects.all()  # Start with all listings

    if form.is_valid():
        bedrooms = form.cleaned_data.get('bedrooms')
        bathrooms = form.cleaned_data.get('bathrooms')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')
        listing_type = form.cleaned_data.get('listing_type')

        # Apply filters
        if bedrooms:
            listings = listings.filter(bedrooms=int(bedrooms))
        if bathrooms:
            listings = listings.filter(bathrooms=int(bathrooms))
        if price_min is not None:
            listings = listings.filter(price__gte=price_min)
        if price_max is not None:
            listings = listings.filter(price__lte=price_max)
        if listing_type:
            listings = listings.filter(listing_type=listing_type)


    context = {
        'form': form,
        'listings': listings,
    }

    return render(request, 'search.html', context)

def index(request):
    
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome, {user.username}! Your account has been created successfully.')
            return redirect("/")
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

