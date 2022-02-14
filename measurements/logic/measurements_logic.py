from ..models import Measurement
def get_measurements():
    measurement=Measurement.objects.all()
    return measurement
def create_measurement(var):
    variable = Measurement(name=var["name"])
    variable.save()
    return variable