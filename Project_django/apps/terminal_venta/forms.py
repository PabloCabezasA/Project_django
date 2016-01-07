from django.forms import ModelForm
from Project_django.apps.terminal_venta.models import Product_product, Terminal_order, Terminal_order_line, Terminal_session
from django.forms.models import inlineformset_factory

class product_product_form(ModelForm):
    def __init__(self, *args, **kwargs ):
        super(product_product_form, self).__init__(*args,**kwargs)
        for key in self.fields.keys():
            if key =='active' or key =='model_pic':
                continue                         
            self.fields[key].widget.attrs = {'class':'form-control'}

    class Meta:
        model = Product_product
        fields = "__all__"
        
class Terminal_orden_form(ModelForm):
    def __init__(self, *args, **kwargs ):
        super(Terminal_orden_form, self).__init__(*args,**kwargs)
        self.fields['amount_total'].widget.attrs = {'readonly':'readonly'}
    class Meta:
        model = Terminal_order
        fields = "__all__"


class Terminal_orden_line_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Terminal_orden_line_form, self).__init__(*args, **kwargs)
        self.fields['qty'].widget.attrs = {'class': 'order_line'}
        self.fields['price_unit'].widget.attrs = {'class': 'order_line'}
        self.fields['amount_total'].widget.attrs = {'readonly':'readonly'}
    class Meta:
        model = Terminal_order_line
        fields = "__all__"

Terminal_order_line_formset = inlineformset_factory(parent_model=Terminal_order, 
                                                    model=Terminal_order_line, 
                                                    form = Terminal_orden_line_form,
                                                    can_delete=True,
                                                    fields="__all__"
                                                    )

class Terminal_session_form(ModelForm):
    class Meta:
        model = Terminal_session
        fields = "__all__"

