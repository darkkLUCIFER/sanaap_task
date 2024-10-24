import django_filters

from apps.tasks.models import Task


class TaskFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')

    created_at = django_filters.DateFilter(method='filter_created_at')
    created_at__gte = django_filters.DateFilter(method='filter_created_at__gte')
    created_at__lte = django_filters.DateFilter(method='filter_created_at__lte')

    def filter_created_at(self, queryset, name, value):
        if value:
            return queryset.filter(created_at__date=value)
        return queryset

    def filter_created_at__gte(self, queryset, name, value):
        if value:
            return queryset.filter(created_at__date__gte=value)
        return queryset

    def filter_created_at__lte(self, queryset, name, value):
        if value:
            return queryset.filter(created_at__date__lte=value)
        return queryset

    class Meta:
        model = Task
        fields = ['title', 'created_at']
