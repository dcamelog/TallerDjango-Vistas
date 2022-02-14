from django.shortcuts import render
from measurements.logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def measurements_view(request):
    if request.method =='GET':
        measurements=ml.get_measurements()
        measurements_dto =serializers.serialize('json',measurements)
        return HttpResponse(measurements_dto,'application/json')
        
    
    
    
