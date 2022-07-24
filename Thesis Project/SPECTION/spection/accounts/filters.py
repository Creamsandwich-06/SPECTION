import django_filters
from django_filters import DateFilter, CharFilter
from django import forms
from .models import *


class DateInput(forms.DateInput):
    input_type = 'date'


class Orderfilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', label=('Date Created'),
                            widget=DateInput(attrs={'type': 'date'}), lookup_expr='gte')
    end_date = DateFilter(field_name='date_created', label=('Date Ended'),
                          widget=DateInput(attrs={'type': 'date'}), lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']

class Newsfilter(django_filters.FilterSet):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['profile_pic', 'date_created']