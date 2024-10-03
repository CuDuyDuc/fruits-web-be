from fruits_web.apps.platforms.serializers_container import serializers, Cart

class AddCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id_product','quantity']
    
    def create(self, validated_data):
        id_product = validated_data.get('id_product')
        user = self.context['request'].user
        try:
            cart_item = Cart.objects.get(id_product=id_product, id_user=user)
            cart_item.quantity += validated_data.get('quantity', 1)
            cart_item.total_money = cart_item.quantity * cart_item.id_product.price  # Giả sử bạn có giá trong Product model
            cart_item.save()
            return cart_item
        except Cart.DoesNotExist:
            cart_item = Cart.objects.create(
                id_product=id_product,
                id_user=user,
                quantity=validated_data.get('quantity', 1),  # Số lượng mặc định là 1
                total_money=validated_data.get('quantity', 1) * id_product.price  # Tính tổng tiền
            )
            return cart_item
        
class UpdateCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['quantity']

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.total_money = instance.quantity * instance.id_product.price
        instance.save()
        return instance