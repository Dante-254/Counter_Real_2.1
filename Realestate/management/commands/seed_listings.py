import random
from django.core.management.base import BaseCommand
from faker import Faker
from Realestate.models import Listing  # Make sure this imports your model

class Command(BaseCommand):
    help = 'Seeds the database with random real estate listings'

    def handle(self, *args, **kwargs):
        fake = Faker()
        listing_types = ['B', 'R']  # 'B' for Buy, 'R' for Rent

        for _ in range(1024):  # Generates 1024 listings
            Listing.objects.create(
                bedrooms=random.randint(1, 5),
                bathrooms=random.randint(1, 3),
                price=random.randint(5000, 5000000),
                listing_type=random.choice(listing_types),
                description=fake.text(),
            )
        self.stdout.write(self.style.SUCCESS('Successfully seeded the database with listings'))
