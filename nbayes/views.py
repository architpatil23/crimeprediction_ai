# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import services
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect, HttpResponse
from .forms import CrimeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/accounts/login/")
def predict_view(request):
    if request.method == 'POST':
        form = CrimeForm(request.POST)
        if form.is_valid():
            crime_details = []
            crime_details.extend((form.cleaned_data['nbd'],form.cleaned_data['dist'],form.cleaned_data['hour'],form.cleaned_data['day']))
            print crime_details
            if(form.cleaned_data['day'] == 'All'):
                crime_result = services.get_prediction_day(form.cleaned_data['nbd'], form.cleaned_data['dist'], form.cleaned_data['hour'], form.cleaned_data['filename'])
                return render(request,'nbayes/result.html', {'crime_result':crime_result, 'crime_details':crime_details})
            elif (form.cleaned_data['hour'] == 'All'):
                crime_result = services.get_prediction_hour(form.cleaned_data['nbd'], form.cleaned_data['dist'], form.cleaned_data['day'], form.cleaned_data['filename'])
                return render(request,'nbayes/result3.html', {'crime_result':crime_result, 'crime_details':crime_details})
            else:
                crime_result = services.get_prediction(form.cleaned_data['nbd'],form.cleaned_data['dist'],form.cleaned_data['hour'],form.cleaned_data['day'],form.cleaned_data['filename'])
                return render(request,'nbayes/result2.html', {'crime_result':crime_result, 'crime_details':crime_details})
    else:
		form = CrimeForm()
		return render(request,'nbayes/predict.html', {'form': form})

@login_required(login_url="/accounts/login/")
def upload_csv(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'nbayes/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'nbayes/simple_upload.html')