import django_filters
from .models import Hospital

class hospitals(django_filters.FilterSet):
    class Meta:
        model = Hospital
        fields = ('name','district')