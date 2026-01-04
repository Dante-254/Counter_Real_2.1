from django import forms

class ListingSearchForm(forms.Form):
    bedrooms = forms.ChoiceField(
        choices=[('', 'Any'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5+')], 
        required=False, 
        label="Bedrooms"
    )
    bathrooms = forms.ChoiceField(
        choices=[('', 'Any'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4+')], 
        required=False, 
        label="Bathrooms"
    )
    price_min = forms.DecimalField(
        required=False, 
        label="Min Price", 
        decimal_places=2, 
        max_digits=10,
        widget=forms.NumberInput(attrs={'placeholder': 'Min price', 'min': '0'})
    )
    price_max = forms.DecimalField(
        required=False, 
        label="Max Price", 
        decimal_places=2, 
        max_digits=10,
        widget=forms.NumberInput(attrs={'placeholder': 'Max price', 'min': '0'})
    )
    listing_type = forms.ChoiceField(
        choices=[('', 'Any'), ('B', 'Buy'), ('R', 'Rent')], 
        required=False, 
        label="Type"
    )