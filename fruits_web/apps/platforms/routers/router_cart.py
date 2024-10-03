from fruits_web.apps.platforms.routers import AddCartViewAPI, path, ListCartViewAPI, UpdateCartViewAPI, DeleteCartViewAPI

urlpatterns = [
    path('addcart/', AddCartViewAPI.as_view(), name= 'addCart'),
    path('listcart/', ListCartViewAPI.as_view(), name= 'listCart'),
    path('updatecart/<uuid:pk>/', UpdateCartViewAPI.as_view(), name= 'updateCart'),
    path('deletecart/<uuid:pk>/', DeleteCartViewAPI.as_view(), name= 'deleteCart'),
]