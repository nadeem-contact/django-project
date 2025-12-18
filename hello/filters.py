import django_filters
from .models import Customer

class CustomerFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')
    phone = django_filters.CharFilter(lookup_expr='icontains')
    location = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Customer
        fields = ['full_name', 'email', 'phone', 'location']
