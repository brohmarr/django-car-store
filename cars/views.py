from django.shortcuts import render
from django.db.models import Q
from cars.models import Car
import locale

# Set the locale for the function below.
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

def format_currency(value):
    """Format the value of a car with thousand separators."""
    return locale.format_string("%d", value, grouping=True)


def home(request):
    return render(request, 'home.html')


def cars_view(request):
    cars = Car.objects.all().order_by('brand__name', 'value')

    for car in cars:
        car.value = format_currency(car.value)

    search_query = request.GET.get('search')

    if search_query:
        cars = cars.filter(Q(model__icontains=search_query) | 
                           Q(brand__name__icontains=search_query))

    context = {
        'cars': cars,
        'search_query': search_query
    }

    return render(request, 'cars.html', context)


def about(request):
    return render(request, 'about.html')
