import uuid

from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import RecoveryCode, User


class CreateUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "first_name", "last_name", "is_supplier"]
        read_only_fields = ["id"]

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)

    def validate(self, data: dict) -> dict:
        user = User.objects.filter(username=data['username']).first()
        if not user or not user.check_password(data['password']):
            raise serializers.ValidationError('Invalid credentials')
        return data

    def get_token(self, validated_data: dict) -> str:
        user = User.objects.filter(username=validated_data['username']).first()
        token = Token.objects.get_or_create(user=user)[0]
        return token.key
    
class RecoveryCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def get_code(self, data: dict) -> dict:
        user = User.objects.filter(email=data['email']).first()
        if not user:
            raise serializers.ValidationError('Invalid email')
        code = RecoveryCode.objects.filter(user=user).order_by('-created_at').first()
        if not code:
            code = RecoveryCode.objects.create(user=user, code=uuid.uuid4())
        return code.code
            
        
class RecoverPasswordSerializer(serializers.Serializer):
    code = serializers.UUIDField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    
    def create(self, validated_data: dict) -> User:
        code = RecoveryCode.objects.filter(code=validated_data['code']).first()
        if not code:
            raise serializers.ValidationError('Invalid code')
        user = User.objects.filter(id=code.user.id).first()
        user.set_password(validated_data['password'])
        user.save()
        return user
        
        
    
        

    
