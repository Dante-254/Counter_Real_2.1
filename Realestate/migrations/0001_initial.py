# Generated by Django 5.0.6 on 2024-09-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('listing_type', models.CharField(choices=[('buy', 'Buy'), ('rent', 'Rent')], max_length=4)),
                ('description', models.TextField()),
            ],
        ),
    ]