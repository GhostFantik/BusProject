from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .forms import GetDataForm
from .Services import SurveysService


# Create your views here.

def index(request):
    context = {}
    if request.method == 'POST':
        form = GetDataForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date'].strftime('%d-%m-%Y')
            user_name = form.cleaned_data['user_name']
            vehicle_plate = form.cleaned_data['vehicle_plate']
            context['data'] = SurveysService.get_surveys(date, user_name, vehicle_plate)
        else:
            raise HttpResponseBadRequest('No valid data!')
    else:
        form = GetDataForm()
    context['form'] = form

    return render(request, 'DbApp/index.html', context)
