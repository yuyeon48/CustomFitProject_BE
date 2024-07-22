from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, ProductSearchViewSet, AddToCartView, CartDetailView

product_router = SimpleRouter()
product_router.register('product', ProductViewSet, basename='product')

urlpatterns = [
    path('', include(product_router.urls)),
    path('search/', ProductSearchViewSet.as_view({'get': 'search'}), name='search'),
    path('search/<int:pk>/', ProductSearchViewSet.as_view({'get': 'retrieve'}), name='search-detail'),
    path('add_cart/<int:product_id>/', AddToCartView.as_view(), name='add_cart'),
    path('cart/', CartDetailView.as_view(), name='cart-detail'),
]
