from .firebase_client import FirebaseClient

def send_order_success_notification(cart_item):
    
    name = cart_item.id_product.name
    data_notification = {
        'title': 'Đơn hàng thành công',
        'body': f'Chào {cart_item.id_user.username}, đơn hàng {name} của bạn đã được đặt thành công!',
    }
    
    device_token = cart_item.id_user.device_token  # Lấy device_token của người dùng

    if device_token:
        firebase_client = FirebaseClient()
        firebase_client.send_notification(data_notification, device_token=device_token)
    else:
        print("Người dùng chưa có device token.")
