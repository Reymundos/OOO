from django.urls import path
from .views import ShoppingListCreateView, ShoppingUpdateDeleteView

urlpatterns = [
    path('shop/', ShoppingListCreateView.as_view()),
    path('shop/<int:pk>', ShoppingUpdateDeleteView.as_view())
]
