from django.core.exceptions import PermissionDenied
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


from apps.user.models import User
from apps.user.serializers import RegisterSerializer, ProfileSerializer, ProfileUpdateSerializer


class RegisterView(CreateAPIView):
    queryset =  User.objects.all() # Model
    serializer_class = RegisterSerializer # Serializer

class ProfileView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    # serializer_class = UserMeReadSerializer
    permission_classes = [IsAuthenticated]  # 인증된 사용자만 데이터 접근 가능
    authentication_classes = [JWTAuthentication]  # JWT 인증

    def get_object(self):
        # DRF 기본 동작
        # URL 통해 넘겨 받은 pk를 통해 queryset에 데이터를 조회
        # -> User.objects.all()
        return self.request.user  # 인증이 끝난 유저가 들어감.

    def get_serializer_class(self):
        # HTTP 메소드 별로 다른 Serializer 적용
        # -> 각 요청마다 입/출력에 사용되는 데이터의 형식이 다르기 때문

        if self.request.method == "GET":
            return ProfileSerializer

        elif self.request.method == "PATCH":
            return ProfileUpdateSerializer

        return super().get_serializer_class()
