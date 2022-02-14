from ..models import Measurement
def get_measurements():
    measurement=Measurement.objects.all()
    return measurement
def create_measurement(var):
    variable = Measurement(name=var["name"])
    variable.save()
    return variable

def update_measurement(measurement_pk, measurement_var):
    measurement = get_measurement()
    measurement.variable = Measurement(name=measurement_var["name"])
    measurement.save()

def delete_measurement(measurement_pk):
    measurement = get_measurement()
    measurement.delete()
