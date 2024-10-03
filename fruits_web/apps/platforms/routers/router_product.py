from fruits_web.apps.platforms.routers import AddProductViewAPI, path, UpdateProductViewAPI, DeleteProductViewAPI

urlpatterns = [
    path('add-products/',AddProductViewAPI.as_view(),name='add'),    
    path('update-product/<uuid:pk>/',UpdateProductViewAPI.as_view(),name='update'),    
    path('delete-product/<uuid:pk>/',DeleteProductViewAPI.as_view(),name='delete'),    
]