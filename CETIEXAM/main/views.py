from django.shortcuts import render
from django.views.generic import CreateView
from .forms import createCounrty, createCity
from django.urls import reverse_lazy
from .models import Country, City
from django.shortcuts import redirect, get_object_or_404
from .forms import CityForm
def base(request):
    return render(request, 'main/base.html')

class create(CreateView):
    form_class = createCounrty
    model = Country
    template_name = 'main/create.html'
    success_url = reverse_lazy('country')

class createsecond(CreateView):
    form_class = createCity
    model = City
    template_name = 'main/createsecond.html'
    success_url = reverse_lazy('createsecond')

def country(request):
    cities = City.objects.all()
    return render(request, 'main/country.html', {'cities': cities})

def city(request):
    cities = City.objects.all()
    return render(request, 'main/city.html', {'cities': cities})


def delete_city(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    city.delete()
    return redirect('http://127.0.0.1:8000/second')

def edit_city(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    if request.method == 'POST':
        form = CityForm(request.POST, instance=city)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/second')
    else:
        form = CityForm(instance=city)
    return render(request, 'main/edit_city.html', {'form': form})