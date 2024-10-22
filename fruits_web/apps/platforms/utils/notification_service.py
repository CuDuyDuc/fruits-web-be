from .firebase_client import FirebaseClient

def send_login_notification(user):
    # Tạo nội dung thông báo
    data_notification = {
        'title': 'Login Notification',
        'body': f'Welcome back, {user.username}!',
    }
    
    device_token = user.device_token  # Lấy device_token của người dùng
    
    if device_token:
        firebase_client = FirebaseClient()
        firebase_client.send_notification(data_notification, device_token=device_token)
    else:
        print("User does not have a device token.")
