import django_filters
from .models import BloodDoner

class blood_doners(django_filters.FilterSet):
    class Meta:
        model = BloodDoner
        fields = ('group','district')