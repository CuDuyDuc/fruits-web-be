from fruits_web.apps.platforms.routers import RegisterView, LoginAPIView, path, DeleteUserViewAPI, UserListView, CreateShopAPIView

urlpatterns = [
    path('register-user/',RegisterView.as_view(),name='register-user'),
    path('login-user/',LoginAPIView.as_view(),name='login-user'),
    path('delete-user/<uuid:pk>/', DeleteUserViewAPI.as_view(), name='delete-user'), 
    path('list-user/', UserListView.as_view(), name='list-user'), 
    path('create-shop/', CreateShopAPIView.as_view(), name='create-shop'), 
]