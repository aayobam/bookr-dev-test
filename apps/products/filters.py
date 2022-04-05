import django_filters as filters
from .models import Product


class TodoFilters(filters.FilterSet):
    """
    filter class for Product
    """
    name = filters.CharField(field_name="title", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = ['name', 'owner']