from fruits_web.apps.platforms.serializers_container import serializers,User,RefreshToken,auth,AuthenticationFailed, make_password

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email', 'image']
              
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=80, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email is already in use.')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('This username is already in use.')
        return attrs
    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password']) 
        user.save() 
        token = RefreshToken.for_user(user).access_token
        return {
            'user': {
                'email': user.email,
                'username': user.username,
            },
            'access_token': str(token),
        }


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255, min_length = 3)
    password = serializers.CharField(max_length= 68, min_length = 6, write_only = True)
    username = serializers.CharField(max_length= 255, min_length = 6, read_only = True)
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
    
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        
        user = auth.authenticate(email = email, password = password)

        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')

        
        return {
            'email': user.email,
            'username': user.username,
            'refresh_token':str(user.tokens().get('refresh')),
            'access_token': str(user.tokens().get('access')),
        }
        
class CreateShopSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=80, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password','role']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric characters')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('This email is already in use.')
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError('This username is already in use.')
        return attrs
    def create(self, validated_data):
        validated_data['role'] = validated_data['role'].lower() 
        user = User(**validated_data)
        user.set_password(validated_data['password']) 
        user.save() 
        refreshToken = RefreshToken.for_user(user)
        return {
            'user': {
                'email': user.email,
                'username': user.username,
                'role': user.role,
            },
            'refresh_token':str(refreshToken),
            'access_token': str(refreshToken.access_token),
        }

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=False)  
    username = serializers.CharField(required=False)  
    password = serializers.CharField(write_only=True, required=False)  
    class Meta:
        model = User
        fields = ['email','password','username','is_active','role']
    def update(self, instance, validated_data):
        instance.email = validated_data.get('email',instance.email)
        instance.username = validated_data.get('username',instance.username)
        instance.is_active = validated_data.get('is_active',instance.is_active)
        instance.role = validated_data.get('role',instance.role)
        if 'password' in validated_data:
            instance.password = make_password(validated_data['password'])
        instance.save()
        return instance