from django.forms.extras.widgets import SelectDateWidget
from django import forms
from django.forms import ModelForm, Form
from Project_django.apps.terminal_venta.models import Product_product, Terminal_order, Terminal_order_line, Terminal_session
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper

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
    def __init__(self, *args, **kwargs ):
        super(Terminal_session_form, self).__init__(*args,**kwargs)
        for key in self.fields.keys():
            self.fields[key].widget.attrs = {'class':'form-control'}
    class Meta:
        model = Terminal_session
        fields = "__all__"


class TerminalSessionFormHelper(FormHelper):
    model = Terminal_session
    form_tag = False
    help_text_inline = True
    form_show_labels = True

class TerminalOrderFormHelper(FormHelper):
    model = Terminal_order
    form_tag = False
    help_text_inline = True
    form_show_labels = True

class ProductProductHelper(FormHelper):
    model = Product_product
    form_tag = False
    help_text_inline = True
    form_show_labels = True    