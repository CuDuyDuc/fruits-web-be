from fruits_web.apps.platforms.serializers_container import serializers, Product, UserSerializer

class AddProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    class Meta:
        model = Product
        fields = ['name','description','image','price','quantity']
    def create(self, validated_data):
        user = self.context['request'].user
        product = Product(id_user=user,**validated_data)
        product.save()
        return product
        
class UpdateProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=False)  
    price = serializers.DecimalField(max_digits=10, decimal_places=2, required = False)
    class Meta:
        model = Product
        fields = ['name','description', 'image','price','quantity']
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.id_user != user:
            raise serializers.ValidationError("Bạn không có quyền sửa sản phẩm này.")
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance
    
class ListProductSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='id_user')
    class Meta: 
        model = Product
        fields = ['id', 'name', 'description', 'image', 'price', 'quantity', 'id_user', 'user']
        
