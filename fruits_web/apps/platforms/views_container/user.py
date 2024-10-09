from fruits_web.apps.platforms.views_container import generics,RegisterSerializer,User,status,LoginSerializer, CreateShopSerializer, UpdateUserSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from fruits_web.apps.platforms.permissions import IsAdmin,IsAuthenticated
from rest_framework import parsers, renderers
from drf_yasg import openapi


class BaseCreateView(generics.CreateAPIView):
    def handle_create(self, request, serializer_class):
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.create(serializer.validated_data)
        return Response(response_data, status=status.HTTP_201_CREATED)

class RegisterView(BaseCreateView):
    queryset = User.objects.all()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = RegisterSerializer
    def create(self, request, *args, **kwargs):
        return self.handle_create(request, self.serializer_class)
    
class LoginAPIView(generics.GenericAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)  
        response_data = serializer.validated_data
        return Response(response_data, status=status.HTTP_200_OK)

class DeleteUserViewAPI(APIView):
    permission_classes = [IsAdmin]
    def delete(self, request, pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
            user.delete()    
            return Response({"message": "Người dùng và tất cả sản phẩm đã được xóa thành công."}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "Người dùng không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserListView(APIView):
    permission_classes = [IsAdmin]
    def get(self, request):
        users = User.objects.all()
        user_data = [{"id": user.id, "username": user.username, "email": user.email,"role": user.role} for user in users]
        return Response(user_data, status=status.HTTP_200_OK)
    
class CreateShopAPIView(generics.CreateAPIView):
    permission_classes = [IsAdmin]
    queryset = User.objects.all()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CreateShopSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.create(serializer.validated_data)
        return Response(response_data, status=status.HTTP_201_CREATED)
    
class UpdateUserViewAPI(APIView):
    permission_classes =[IsAdmin]
    queryset = User.objects.all()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = UpdateUserSerializer
    @swagger_auto_schema(
        operation_description="Cập nhật người dùng bằng UUID và nhập dữ liệu trong body JSON",
        request_body=UpdateUserSerializer,
        responses={200: "Cập nhật thành công", 404: "Người dùng không tồn tại"}
    )
    def put(self, request,pk, *args, **kwargs):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Người dùng không tồn tại."}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(user, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user_updated = serializer.save() 
        return Response({
            'message': 'Cập nhật thành công',
            'data': {
                'email': user_updated.email,
                'username': user_updated.username,
                'is_active': user_updated.is_active,
                'role': user_updated.role
            }
        }, status=status.HTTP_200_OK)
        
class SearchUserViewAPI(generics.ListAPIView):
    permission_classes = [IsAdmin]
    serializer_class = UserSerializer
    
    id_param = openapi.Parameter('id', openapi.IN_QUERY, description="UUID of the user", type=openapi.TYPE_STRING)
    username_param = openapi.Parameter('username', openapi.IN_QUERY, description="Username of the user", type=openapi.TYPE_STRING)
    email_param = openapi.Parameter('email', openapi.IN_QUERY, description="Email of the email", type=openapi.TYPE_STRING)
    
    @swagger_auto_schema(manual_parameters=[id_param, username_param, email_param])
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        
        user_id = request.query_params.get('id', None)
        username = request.query_params.get('username', None)
        email = request.query_params.get('email', None)
        
        if user_id:
            users = users.filter(id=user_id)
        if username:
            users = users.filter(name__icontains=username)
        if email:
            users = users.filter(price=email)

        if not users.exists():
            return Response({"message": "Không có sản phẩm nào thỏa mãn điều kiện tìm kiếm."}, status=404)

        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)
    
class GetUserById(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, pk, *args, **kwargs):
        user = request.user
        if user.id != pk:
            return Response({"message": "Bạn không có quyền xem"}, status=status.HTTP_403_FORBIDDEN)
        
        try:
            user_by_id = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"message": "Không tìm thấy"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(user_by_id)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
            
            
        