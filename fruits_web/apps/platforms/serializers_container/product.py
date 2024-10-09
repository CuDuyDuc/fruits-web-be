from fruits_web.apps.platforms.serializers_container import serializers, Product

class AddProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description','price','quantity']
    def create(self, validated_data):
        user = self.context['request'].user
        product = Product(id_user=user,**validated_data)
        product.save()
        return product
        
class UpdateProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','description','price','quantity']
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.id_user != user:
            raise serializers.ValidationError("Bạn không có quyền sửa sản phẩm này.")
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
    
class ListProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields = ['id', 'name', 'description', 'price', 'quantity']