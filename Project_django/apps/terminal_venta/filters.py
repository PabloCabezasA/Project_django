# filters.py
import django_filters
from .models import Terminal_order, Terminal_session, Product_product


class TerminalOrderFilter(django_filters.FilterSet):
    class Meta:
        model = Terminal_order
        order_by = ['pk']

class TerminalSessionFilter(django_filters.FilterSet):
    class Meta:
        model = Terminal_session
        order_by = ['pk']

class ProductProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product_product
        order_by = ['pk']