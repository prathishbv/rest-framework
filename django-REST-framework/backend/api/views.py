from django.forms.models import model_to_dict
from product.models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response

from product.serializers import ProductSerializer

@api_view(["GET"])
def api_path(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=["id", "title", "price"])
        data = ProductSerializer(instance).data
        # data["id"] = models_data.id
        # data["title"] = models_data.title
        # data["content"] = models_data.content
        # data["price"] = models_data.price
        
    print(data)
    return Response(data)
