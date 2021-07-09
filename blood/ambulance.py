import django_filters
from .models import Ambulance

class ambulances(django_filters.FilterSet):
    class Meta:
        model = Ambulance
        fields = ('driver_name','district','hospital')