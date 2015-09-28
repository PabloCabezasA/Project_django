from django.forms import ModelForm
from Project_django.apps.terminal_venta.models import Product_product, Terminal_order, Terminal_order_line
from django.forms.models import inlineformset_factory


class product_product_form(ModelForm):
    class Meta:
        model = Product_product
        fields = "__all__"
        
class Terminal_orden_form(ModelForm):
    class Meta:
        model = Terminal_order
        fields = "__all__"

class Terminal_orden_line_form(ModelForm):
    class Meta:
        model = Terminal_order_line
        fields = "__all__"

Terminal_order_line_formset = inlineformset_factory(Terminal_order, 
                                                    Terminal_order_line, 
                                                    can_delete=True,
                                                    fields="__all__"
                                                    )