from fruits_web.apps.platforms.serializers_container import serializers

class NotificationSerializer(serializers.Serializer): 
    device_token = serializers.CharField(required=True, max_length=255, help_text="Device token for sending the notification.")
    notification_body = serializers.CharField(required=True, max_length=500, help_text="Body of the notification.")
    notification_title = serializers.CharField(required=True, max_length=100, help_text="Title of the notification.")

    def validate_device_token(self, value):
        if not value:
            raise serializers.ValidationError("Device token is required.")
        return value

    def validate(self, attrs):

        return attrs