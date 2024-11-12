from django.shortcuts import render
from django.db.models import Q
from cars.models import Car
import locale

# Set the locale for formatting.
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_currency(value):
    """Format the value of a car with thousand separators."""
    return locale.format_string("%d", value, grouping=True)


def cars_view(request):
    # Get all available cars in the database ordered by brand and value.
    cars = Car.objects.all().order_by('brand__name', 'value')

    for car in cars:
        car.value = format_currency(car.value)

    # Get the search parameter from the user.
    search_query = request.GET.get('search')

    # Filter results by model and brand.
    if search_query:
        cars = cars.filter(Q(model__icontains=search_query) | 
                           Q(brand__name__icontains=search_query))

    # Set the page's context.
    context = {
        'cars': cars,
        'search_query': search_query
    }

    # Rendering the page.
    return render(request, 'cars.html', context)
