from ..models import Measurement
def get_measurements():
    measurement=Measurement.objects.all()
    return measurement

def get_measurement(var_pk):
    measurement=Measurement.objects.get(Unit=var_pk)
    return measurement

def create_measurement(var):
    print(f"==================================================\n{var}\n============================================================")
    variable = Measurement(unit=var["unit"])
    variable.save()
    return variable

def update_measurement(measurement_pk, measurement_var):
    measurement = get_measurement()
    measurement.variable = Measurement(name=measurement_var["name"])
    measurement.save()

def delete_measurement(measurement_pk):
    measurement = get_measurement()
    measurement.delete()
