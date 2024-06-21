from .serializer import Shopping, ShoppingSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class ShoppingListCreateView(ListCreateAPIView):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ShoppingUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Shopping.objects.all()
    serializer_class = ShoppingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]