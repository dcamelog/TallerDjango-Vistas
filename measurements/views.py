from django.shortcuts import render
import measurements
from measurements.logic import measurements_logic as ml
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def measurements_view(request, pk):
    if request.method =='GET':
        id=request.GET.get("id",None)
        if id:    
            measurement=ml.get_measurement(id)
            measurement_dto=serializers.serialize('json',measurement)
            return HttpResponse(measurement_dto,'application/json')
        else:
            measurements=ml.get_measurements()
            measurements_dto =serializers.serialize('json',measurements)
            return HttpResponse(measurements_dto,'application/json')
    if request.method == 'POST':
        variable_dto = ml.create_measurement(json.loads(request.body))
        variable = serializers.serialize('json', [variable_dto,])
        return HttpResponse(variable, 'application/json')
    if request.method == 'PUT':
        measurement_dto = ml.update_measurement(pk,json.loads(request.body))
        measurement = serializers.serialize('jason', [measurement_dto,])
        return HttpResponse(measurement, 'application/jason')
    if request.method == 'DELETE':
        measurement_dto = ml.delete_measurement(pk,json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
        
        
    
    
    
