from django import forms
from django.shortcuts import render
from .models import Listing
from .forms import ListingSearchForm

class SearchForm(forms.Form):
    bedrooms = forms.ChoiceField(choices=[('', 'Any'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])
    bathrooms = forms.ChoiceField(choices=[('', 'Any'), (1, '1'), (2, '2'), (3, '3')])
    price_min = forms.IntegerField(required=False)
    price_max = forms.IntegerField(required=False)
    listing_type = forms.ChoiceField(choices=[('', 'Any'), ('buy', 'Buy'), ('rent', 'Rent')])

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

        if listing_type:
            listings = listings.filter(listing_type=listing_type)
            print(f'Filtered by listing_type: {listings.query}')  # Debug

    context = {
        'form': form,
        'listings': listings,
    }

    return render(request, 'search.html', context)




def index(request):
    
    return render(request, 'index.html')

def aboutus(request):
    return render(request, 'aboutus.html')



