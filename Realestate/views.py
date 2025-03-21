from django import forms
from django.shortcuts import render, redirect
from .models import Listing
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import ListingSearchForm
from django.contrib.auth.forms import UserCreationForm


class SearchForm(forms.Form):
    bedrooms = forms.ChoiceField(choices=[('', 'Any'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], required=False)
    bathrooms = forms.ChoiceField(choices=[('', 'Any'), (1, '1'), (2, '2'), (3, '3')], required=False)
    price_min = forms.IntegerField(required=False)
    price_max = forms.IntegerField(required=False)
    listing_type = forms.ChoiceField(choices=[('', 'Any'), ('B', 'Buy'), ('R', 'Rent')], required=False)

def search(request):
    form = SearchForm(request.GET)
    listings = Listing.objects.all()  # Start with all listings

    if form.is_valid():
        bedrooms = form.cleaned_data.get('bedrooms')
        bathrooms = form.cleaned_data.get('bathrooms')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')
        listing_type = form.cleaned_data.get('listing_type')

        # Apply filters and print the query at each step for debugging
        if bedrooms:
            listings = listings.filter(bedrooms=bedrooms)
        if bathrooms:
            listings = listings.filter(bathrooms=bathrooms)
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
            return redirect("/")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

