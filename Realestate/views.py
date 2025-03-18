from django import forms
from django.shortcuts import render, redirect
from .models import Listing
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import ListingSearchForm
from django.contrib.auth.forms import UserCreationForm
from .models import Counter


class SearchForm(forms.Form):
    bedrooms = forms.ChoiceField(choices=[('', 'Any'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], required=False)
    bathrooms = forms.ChoiceField(choices=[('', 'Any'), (1, '1'), (2, '2'), (3, '3')], required=False)
    price_min = forms.IntegerField(required=False)
    price_max = forms.IntegerField(required=False)
    listing_type = forms.ChoiceField(choices=[('', 'Any'), ('buy', 'Buy'), ('rent', 'Rent')], required=False)

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
            print(f'Filtered by bedrooms: {listings.query}')  # Debug

        if bathrooms:
            listings = listings.filter(bathrooms=bathrooms)
            print(f'Filtered by bathrooms: {listings.query}')  # Debug

        if price_min is not None:
            listings = listings.filter(price__gte=price_min)
            print(f'Filtered by price_min: {listings.query}')  # Debug

        if price_max is not None:
            listings = listings.filter(price__lte=price_max)
            print(f'Filtered by price_max: {listings.query}')  # Debug

        # if listing_type:
        #     listings = listings.filter(listing_type=listing_type)
        #     print(f'Filtered by listing_type: {listings.query}')  # Debug

    context = {
        'form': form,
        'listings': listings,
    }

    return render(request, 'search.html', context)




def index(request):
    
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')


@login_required
def counter_view(request):
    counter, created = Counter.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        if "increment" in request.POST:
            counter.value += 1
        elif "decrement" in request.POST:
            counter.value -= 1
        elif "reset" in request.POST:
            counter.value = 0
        counter.save()

    return render(request, "index.html", {"counter": counter})

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

