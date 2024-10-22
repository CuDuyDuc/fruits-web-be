from firebase_admin import messaging
from rest_framework import status
from fruits_web.apps.platforms.views_container import NotificationSerializer,Response,generics
from rest_framework import parsers, renderers



class SendNotificationView(generics.CreateAPIView):
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.FileUploadParser)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = NotificationSerializer
    def post(self, request, *args, **kwargs):
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            device_token = serializer.validated_data['device_token']
            notification_title = serializer.validated_data['notification_title']
            notification_body = serializer.validated_data['notification_body']

            message = messaging.Message(
                notification=messaging.Notification(
                    title=notification_title,
                    body=notification_body,
                ),
                token=device_token,
            )

            try:
                response = messaging.send(message)
                return Response({'message_id': response}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)