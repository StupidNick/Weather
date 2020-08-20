from .models import Temperature
from django_filters import rest_framework as filters
import django_filters




class DateFilter(filters.FilterSet):
	date = django_filters.DateRangeFilter()
	date_min = filters.DateFilter(field_name='date', lookup_expr='gte')
	date_max = filters.DateFilter(field_name='date', lookup_expr='lte')
	
	class Meta:
		model = Temperature
		fields = ['date_min', 'date_max', 'date']