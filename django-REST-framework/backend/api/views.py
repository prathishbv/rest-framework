from django.forms.models import model_to_dict
from product.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.serializers import ProductSerializer

@api_view(["POST"])
def api_path(request, *args, **kwargs):
    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)

    return Response({"Invalid": "not good data"})