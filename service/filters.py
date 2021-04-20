import django_filters
from django.db.models import Q
from service.models import Service
from django_filters.filters import CharFilter


class serviceFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method='my_custom_filter', label=False)

    class Meta:
        model = Service
        fields = ['search']

    def my_custom_filter(self, queryset, name, value):
        return Service.objects.filter(
            Q(name__icontains=value) | Q(description__icontains=value)
        )