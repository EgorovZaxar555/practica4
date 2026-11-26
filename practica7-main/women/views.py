from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Women
from .serializers import WomenSerializer

API_URL = 'http://127.0.0.1:8000/api/v1/womenlist/'

class WomenAPIView(generics.ListAPIView):
    queryset = Women.objects.filter(is_published=True).order_by('id')
    serializer_class = WomenSerializer
    permission_classes = [AllowAny]
    pagination_class = None


