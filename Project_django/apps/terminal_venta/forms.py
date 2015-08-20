from django.forms import ModelForm
from Project_django.apps.terminal_venta.models import Product_product



class product_product_form(ModelForm):
    class Meta:
        model = Product_product
        fields = "__all__"