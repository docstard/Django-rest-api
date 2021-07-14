import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class UserFilter(django_filters.FilterSet):

    class Meta:
        model = User_api
        fields = ('__all__')