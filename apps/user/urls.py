
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import viewsemail
from .views import RegisterView, ProfileView, LogoutAPIView, verify_email

app_name = 'user'

urlpatterns = [
    # Auth
    # path('signup/', viewsemail.SignupView.as_view(), name='signup'),
    # path('signup/done/', TemplateView.as_view(template_name='auth/signup_done.html'), name='signup_done'),
    # path('verify/', viewsemail.verify_email, name='verify_email'),
    # path('login/', viewsemail.LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),

    path("signup/", RegisterView.as_view(), name="signup"),

    path('verify/', verify_email, name='verify_email'),
    # POST /api/users/login/ -> 로그인
    path("login/", TokenObtainPairView.as_view(), name="login"),
    # POST /api/users/login/ -> 로그아웃
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    # GET /api/users/profile/ -> 내 프로필 조회
    # PATCH /api/users/me/ -> 내 프로필 수정
    path('profile/', ProfileView.as_view(), name="profile"),

    # JWT
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),

]