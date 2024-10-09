from fruits_web.apps.platforms.routers import AddProductViewAPI, path, UpdateProductViewAPI, DeleteProductViewAPI, ListProductAPIView, SearchProductAPIView

urlpatterns = [
    path('add-product/',AddProductViewAPI.as_view(),name='add'),    
    path('list-product/',ListProductAPIView.as_view(),name='list'),    
    path('update-product/<uuid:pk>/',UpdateProductViewAPI.as_view(),name='update'),    
    path('delete-product/<uuid:pk>/',DeleteProductViewAPI.as_view(),name='delete'),   
    path('search-product/', SearchProductAPIView.as_view(), name='search'), 
]