from fruits_web.apps.platforms.views_container import generics, Cart, AddCartSerializer, Response, status, UpdateCartSerializer
from fruits_web.apps.platforms.permissions import IsUser
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

class AddCartViewAPI (generics.CreateAPIView):
    permission_classes = [IsUser] 
    queryset = Cart.objects.all()
    serializer_class = AddCartSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Lưu sản phẩm vào cơ sở dữ liệu
        return Response({
            'message': 'Thêm thành công',
            'data': serializer.data  # Trả về dữ liệu đã lưu
        }, status=status.HTTP_201_CREATED)
        
class ListCartViewAPI(generics.ListAPIView):
    permission_classes = [IsUser]
    serializer_class = AddCartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(id_user=user)
        
class UpdateCartViewAPI(APIView):
    permission_classes = [IsUser]
    queryset = Cart.objects.all()
    serializer_class = UpdateCartSerializer

    @swagger_auto_schema(
        operation_description="Cập nhật giỏ hàng bằng UUID và nhập dữ liệu trong body JSON",
        request_body= UpdateCartSerializer,
        responses={200: "Cập nhật thành công", 404: "Sản phẩm không tồn tại"}
    )
    def put(self, request, pk, *args, **kwargs):
        try:
            cart_item = Cart.objects.get(pk=pk, id_user=request.user)
        except Cart.DoesNotExist:
            return Response({"error": "Sản phẩm trong giỏ không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(cart_item, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'Cập nhật giỏ hàng thành công',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

class DeleteCartViewAPI(generics.DestroyAPIView):
    permission_classes = [IsUser]
    queryset = Cart.objects.all()

    def delete(self, request, pk, *args, **kwargs):
        try:
            cart_item = Cart.objects.get(pk=pk, id_user=request.user)
        except Cart.DoesNotExist:
            return Response({"error": "Sản phẩm trong giỏ không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        
        cart_item.delete()
        return Response({"message": "Xóa sản phẩm khỏi giỏ hàng thành công."}, status=status.HTTP_200_OK)