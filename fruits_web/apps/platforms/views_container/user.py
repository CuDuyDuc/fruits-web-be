from fruits_web.apps.platforms.views_container import generics,RegisterSerializer,User,status,LoginSerializer, CreateShopSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from fruits_web.apps.platforms.permissions import IsAdmin


class BaseCreateView(generics.CreateAPIView):
    def handle_create(self, request, serializer_class):
        serializer = serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.create(serializer.validated_data)
        return Response(response_data, status=status.HTTP_201_CREATED)

class RegisterView(BaseCreateView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def create(self, request, *args, **kwargs):
        return self.handle_create(request, self.serializer_class)
    
class LoginAPIView(generics.GenericAPIView):
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
    serializer_class = CreateShopSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response_data = serializer.create(serializer.validated_data)
        return Response(response_data, status=status.HTTP_201_CREATED)