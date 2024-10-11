from fruits_web.apps.platforms.views_container import generics, Product, AddProductSerializer, Response, status, UpdateProductSerializer, ListProductSerializer
from fruits_web.apps.platforms.permissions import IsShop, IsAuthenticated, IsUser
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import parsers, renderers
from rest_framework.pagination import LimitOffsetPagination

class AddProductViewAPI(generics.CreateAPIView):
    permission_classes = [IsShop] 
    queryset = Product.objects.all()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AddProductSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # Lưu sản phẩm vào cơ sở dữ liệu
        return Response({
            'message': 'Thêm thành công',
            'data': serializer.data  # Trả về dữ liệu đã lưu
        }, status=status.HTTP_201_CREATED)
    
class ListProductAPIView(generics.ListAPIView):
    permission_classes = [IsShop]
    serializer_class = ListProductSerializer
    pagination_class = None
    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Product.objects.all()
        return Product.objects.filter(id_user = user)

class UpdateProductViewAPI(APIView):
    permission_classes = [IsShop]
    queryset = Product.objects.all()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = UpdateProductSerializer

    def handle_update(self, request, product, partial=False):
        user = request.user
        if product.id_user != user:
            return Response({"error": "Bạn không có quyền sửa sản phẩm này."}, status=status.HTTP_403_FORBIDDEN)
        
        serializer = self.serializer_class(product, data=request.data, partial=partial, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'message': 'Cập nhật thành công',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        operation_description="Cập nhật toàn bộ thông tin sản phẩm bằng UUID và nhập dữ liệu trong body JSON",
        request_body=UpdateProductSerializer,
        responses={200: "Cập nhật thành công", 404: "Sản phẩm không tồn tại"}
    )
    def put(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Sản phẩm không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        
        return self.handle_update(request, product, partial=False)

    @swagger_auto_schema(
        operation_description="Cập nhật một phần thông tin sản phẩm bằng UUID",
        request_body=UpdateProductSerializer,
        responses={200: "Cập nhật thành công", 404: "Sản phẩm không tồn tại"}
    )
    def patch(self, request, pk, *args, **kwargs):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"error": "Sản phẩm không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        
        return self.handle_update(request, product, partial=True)

        
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
    
class SearchProductAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ListProductSerializer
    pagination_class = None
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description="UUID of the product", type=openapi.TYPE_STRING)
    name_param = openapi.Parameter('name', openapi.IN_QUERY, description="Name of the product", type=openapi.TYPE_STRING)
    price_param = openapi.Parameter('price', openapi.IN_QUERY, description="Price of the product", type=openapi.TYPE_NUMBER)
    @swagger_auto_schema(manual_parameters=[id_param, name_param, price_param])
    def get(self, request, *args, **kwargs):
        products = Product.objects.all()
        
        product_id = request.query_params.get('id', None)
        name = request.query_params.get('name', None)
        price = request.query_params.get('price', None)
    
        if product_id:
            products = products.filter(id=product_id)
        if name:
            products = products.filter(name__icontains=name)
        if price:
            products = products.filter(price=price)

        if not products.exists():
            return Response({"message": "Không có sản phẩm nào thỏa mãn điều kiện tìm kiếm."}, status=404)

        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)
    
class ListProductOffsets(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ListProductSerializer
    pagination_class =LimitOffsetPagination 
    def get(self,request): 
        queryset = self.filter_queryset(self.get_queryset())
        # Lọc queryset
        page = self.paginate_queryset(queryset)
        # check page có điều kiện truyền vào hay không nếu không sẽ trả ra tất cả
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
