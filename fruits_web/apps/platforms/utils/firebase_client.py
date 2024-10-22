import os
from firebase_admin import credentials, initialize_app, messaging, _apps

class FirebaseClient:
    def __init__(self):
        self._initialize_firebase_app()

    @staticmethod
    def _initialize_firebase_app():
        # Kiểm tra nếu Firebase đã được khởi tạo trước đó chưa
        if not _apps:
            current_directory = os.getcwd()
            service_account_json = os.path.join(current_directory, 'fruist-web-firebase-adminsdk.json')
            cred = credentials.Certificate(service_account_json)
            initialize_app(cred)  # Khởi tạo Firebase nếu chưa khởi tạo

    @staticmethod
    def send_notification(data_notification: dict, data: dict = {}, device_token: str = None):
        notification = messaging.Notification(**data_notification)
        if device_token:
            message = messaging.Message(notification=notification, token=device_token, data=data)
            response = messaging.send(message)  # Gửi thông báo sau khi chắc chắn Firebase đã khởi tạo rồi
            return response
        print("No device_token provided.")
        return None
