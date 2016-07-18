import django_tables2 as tables
from django_tables2.utils import A
from .models import Terminal_order, Terminal_session, Product_product


class TerminalOrderTable(tables.Table):
    class Meta:
        model = Terminal_order

class TerminalSessionTable(tables.Table):
    class Meta:
        model = Terminal_session

class ProductProductTable(tables.Table):
    class Meta:
        model = Product_product