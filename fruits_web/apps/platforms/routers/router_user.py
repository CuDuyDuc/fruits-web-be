from fruits_web.apps.platforms.routers import RegisterView, LoginAPIView, path, DeleteUserViewAPI, UserListView, CreateShopAPIView, UpdateUserViewAPI, SearchUserViewAPI,GetUserById

urlpatterns = [
    path('register-user/',RegisterView.as_view(),name='register-user'),
    path('login-user/',LoginAPIView.as_view(),name='login-user'),
    path('delete-user/<uuid:pk>', DeleteUserViewAPI.as_view(), name='delete-user'), 
    path('list-user/', UserListView.as_view(), name='list-user'), 
    path('search-user/', SearchUserViewAPI.as_view(), name='search-user'), 
    path('create-shop/', CreateShopAPIView.as_view(), name='create-shop'), 
    path('update-shop/<uuid:pk>', UpdateUserViewAPI.as_view(), name='update-shop'), 
    path('get-use-by-id/<uuid:pk>', GetUserById.as_view(), name='get-user-by-id'), 
]