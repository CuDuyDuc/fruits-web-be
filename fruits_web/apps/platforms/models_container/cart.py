from fruits_web.apps.platforms.models_container import models, uuid, User, Product

class Cart(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.PositiveIntegerField(default=0)  
    total_money = models.DecimalField(max_digits=10, decimal_places=2)  
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart')  # Khóa ngoại user_id liên kết đến bảng User
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Carts'
    