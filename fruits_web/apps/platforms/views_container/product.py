from fruits_web.apps.platforms.views_container import generics, Product, AddProductSerializer, Response, status, UpdateProductSerializer
from fruits_web.apps.platforms.permissions import IsShop
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class AddProductViewAPI(generics.CreateAPIView):
    permission_classes = [IsShop] 
    queryset = Product.objects.all()
    serializer_class = AddProductSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Lưu sản phẩm vào cơ sở dữ liệu
        return Response({
            'message': 'Thêm thành công',
            'data': serializer.data  # Trả về dữ liệu đã lưu
        }, status=status.HTTP_201_CREATED)
    

class UpdateProductViewAPI(APIView):
    permission_classes = [IsShop] 
    queryset = Product.objects.all()
    serializer_class = UpdateProductSerializer
    
    @swagger_auto_schema(
        operation_description="Cập nhật sản phẩm bằng UUID và nhập dữ liệu trong body JSON",
        request_body=UpdateProductSerializer,
        responses={200: "Cập nhật thành công", 404: "Sản phẩm không tồn tại"}
    )
    def put(self, request,pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Sản phẩm không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(product, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'Cập nhật thành công',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
        
class DeleteProductViewAPI(APIView):
    permission_classes = [IsShop]
    def delete(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Sản phẩm không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        user = request.user
        if product.id_user.id != user.id:
            return Response({"error": "Bạn không có quyền xóa sản phẩm này."}, status=status.HTTP_403_FORBIDDEN)
        product.delete()
        return Response({"message": "Xóa sản phẩm thành công."}, status=status.HTTP_200_OK)