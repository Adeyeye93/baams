from django.urls import path, re_path
from . import views

urlpatterns = [
    path('feed/', views.feed, name="feed"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('UpdateItem/', views.update_item, name="UpdateItem"),
    path('shop', views.shop_listing, name="shop"),
    path('bags', views.bag_listing, name="bags"),
    path('shoes', views.shoes_listing, name="shoes"),
    re_path(r'^product_details/(?P<id>\d+)/$', views.productDetail, name="product_details")
]