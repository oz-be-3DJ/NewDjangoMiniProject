from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

User = get_user_model()

# class UsernameSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ['username']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "name", "nickname"]
        read_only_fields = ["id"]
        extra_kwargs = {
            'password': {'write_only':True},  # write_only : 쓰기만 되고 읽어 오진 않음.
            "phone_number": {"required": False, "allow_blank": True}
        }

    def create(self, validated_data):
        # create_user() -> 비밀번호 해싱
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],
            nickname=validated_data['nickname'],
            is_active = True
        )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "password", "name", "nickname", "phone_number"]
        read_only_fields = ["id"]
        extra_kwargs = {
            'password': {'write_only':True},  # write_only : 쓰기만 되고 읽어 오진 않음.
            "phone_number": {"required": False, "allow_blank": True}
        }

    def update(self, instance, validated_data):
        if password := validated_data.get("password"):
            validated_data["password"] = make_password(password)
        return super().update(instance, validated_data)
