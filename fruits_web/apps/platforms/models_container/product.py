from fruits_web.apps.platforms.models_container import models, uuid, User
import os,random
def random_image_filename(instance, filename):
        extension = filename.split('.')[-1]
        new_filename = f"{random.randint(10000000, 99999999)}.{extension}"
        return os.path.join('products/', new_filename)
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)  
    description = models.TextField(null=True, blank=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    quantity = models.PositiveIntegerField(default=0)  
    image = models.ImageField(upload_to=random_image_filename,default='image.png')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)  
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')  # Khóa ngoại user_id liên kết đến bảng User

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def __str__(self):
        return self.name