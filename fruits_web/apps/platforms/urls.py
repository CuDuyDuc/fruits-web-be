from django.urls import path,include


urlpatterns = [
    path('user/',include('fruits_web.apps.platforms.routers.router_user')),
    path('product/',include('fruits_web.apps.platforms.routers.router_product')),
    path('cart/',include('fruits_web.apps.platforms.routers.router_cart')),
]


