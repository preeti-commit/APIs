from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    Address = serializers.CharField(max_length=128, min_length=8)
    mobile = serializers.CharField(max_length=128, min_length=8 )
    email = serializers.EmailField(max_length=128, min_length=4 )

    class Meta:
        model = User
        fields = ['password', 'Address', 'mobile', 'email']

    # def validate(self, attrs):
    #     email = attrs.get('email','')
    #     if User.objects.filter(email=email).exists():
    #         raise serializers.ValidationError(
    #             {'email',('Email is already in use')})
    #     return super().validate(attrs)
    #
    # def create(self, validated_data):
    #     return User.objects.create_user(validated_data)




class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    # token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        fields = ('email','password')

