from django.urls import path,include
from fruits_web.apps.platforms.views_container import SendNotificationView

urlpatterns = [
    path('user/',include('fruits_web.apps.platforms.routers.router_user')),
    path('product/',include('fruits_web.apps.platforms.routers.router_product')),
    path('cart/',include('fruits_web.apps.platforms.routers.router_cart')),
    path('send/', SendNotificationView.as_view(), name='sendnotification'),
]


