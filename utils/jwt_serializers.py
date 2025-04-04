from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class BankTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['email'] = user.email  # 토큰에 유저 정보를을 함께 담아서 보냄
        token['nickname'] = user.nickname
        token['name'] = user.name
        token['phone_number'] = user.phone_number

        return token

# 토큰 정보 확인
# https://jwt.io/