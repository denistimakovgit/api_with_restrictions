from django_filters import rest_framework as filters
import django_filters
from django.db import models as django_models
from .models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = filters.DateTimeFromToRangeFilter(field_name="created_at")

    class Meta:
        model = Advertisement
        fields = ["created_at"]

    filter_overrides = {
        django_models.DateTimeField: {
            'filter_class': django_filters.IsoDateTimeFilter
        },
    }