from django.shortcuts import render
from django.db.models import Q
from cars.models import Car


def cars_view(request):
    cars = Car.objects.all()
    search = request.GET.get('search')

    # Filtering results by model and name.
    if search:
        cars = cars.filter(Q(model__icontains=search) | 
                           Q(brand__name__icontains=search)).order_by('brand__name')

    return render(request,
                  'cars.html',
                  {'cars': cars}
    )
