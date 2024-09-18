from django import forms

class ListingSearchForm(forms.Form):
    bedrooms = forms.IntegerField(required=False, label="Bedrooms")
    bathrooms = forms.IntegerField(required=False, label="Bathrooms")
    price_min = forms.DecimalField(required=False, label="Min Price", decimal_places=2, max_digits=10)
    price_max = forms.DecimalField(required=False, label="Max Price", decimal_places=2, max_digits=10)
    listing_type = forms.ChoiceField(choices=[('', 'Any'), ('buy', 'Buy'), ('rent', 'Rent')], required=False, label="Type")