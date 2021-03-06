from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from Project_django.apps.terminal_venta.models import Product_product, Terminal_order, Terminal_order_line
import simplejson

class ProductSerializer(serializers.ModelSerializer):
    class Meta():
        model = Product_product

class ProductSerializerList(APIView):
    """
    List all Products, or create a new product.
    """    
        
    def get(self, request, format=None):
        snippets = Product_product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductSerializerDetail(APIView):
    """
    Retrieve, update or delete a Product instance.
    """
    def get_object(self, pk):
        try:
            return Product_product.objects.get(pk=pk)
        except Product_product.DoesNotExist:
            raise Http404

    def get_product_id(self, name, code):
        products = Product_product.objects.filter(name=name, code=code) 
        if products:
            return products[0].id
        else:
            return False 

    def get_product_object(self, name):
        products = Product_product.objects.filter(name__icontains=name) 
        if products:
            return products
        else:
            raise Http404

    def get(self, request, pk=None, name=None, code=None, format=None):
        if name and code:
            id = self.get_product_id(name, code)
            return Response(simplejson.dumps({ 'id' :id}))
        elif name:
            products = self.get_product_object(name)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)            
        elif pk:
            product = self.get_object(pk)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        return Response(simplejson.dumps({'Error': 'Bad Call'}))
    
    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderLineSerializer(serializers.ModelSerializer):
    class Meta():
        model = Terminal_order_line
        fields = (
            'product_id', 'qty', 'price_unit', 'amount_total'
        )
        extra_kwargs = {
            "id": {
                "read_only": False,
                "required": False,
            },
        }
        

class OrderSerializer(serializers.ModelSerializer):
    lines = OrderLineSerializer(many=True)
    class Meta():
        model = Terminal_order
        fields = (
            'name', 'date_order', 'amount_total', 'session_id', 'lines'
        )

    def create(self, validated_data):
        lines_data = validated_data.pop('lines')
        ticket = Terminal_order.objects.create(**validated_data)
        for line_data in lines_data:
            Terminal_order_line.objects.create(order_id=ticket, **line_data)
        return ticket
        
    
class OrderSerializerList(APIView):
    """
    List all Orders, or create a new order.
    """
    def get(self, request, format=None):
        snippets = Terminal_order.objects.all()
        serializer = OrderSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        req_data = request.data.copy()
        req_data = simplejson.loads(req_data.keys()[0])        
        serializer = OrderSerializer(data = req_data) 
        print serializer.initial_data 
        if serializer.is_valid():            
            print serializer.validated_data            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: