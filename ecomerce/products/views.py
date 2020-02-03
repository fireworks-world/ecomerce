from django.http import HttpResponse
from rest_framework import viewsets
from .models import Products
from .serializers import ProductSerializer


# def home(request):
#     return HttpResponse("HelloWorld")

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

# Create your views here.
