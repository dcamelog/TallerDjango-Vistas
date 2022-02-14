from ..models import Measurement
def get_measurements():
    measurement=Measurement.objects.all()
    return measurement