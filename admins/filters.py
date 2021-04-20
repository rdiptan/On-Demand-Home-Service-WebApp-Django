import django_filters
from django.db.models import Q
from order.models import Order
from django_filters.filters import CharFilter


class OrderFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='my_custom_filter', label=False)

    class Meta:
        model = Order
        fields = ['q']

    def my_custom_filter(self, queryset, name, value):
        return Order.objects.filter(
            Q(address__icontains=value) | Q(street__icontains=value) | Q(status__icontains=value)
        )
    