from .base import *

DEBUG = False

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    # "13.124.181.116",  # EC2 퍼블릭 IP
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bank',        # 생성한 DB 이름
        'USER': 'root',          # PostgreSQL 사용자
        'PASSWORD': '1234',      # 비밀번호
        'HOST': 'localhost',     # 로컬에서 실행 중이므로 localhost
        'PORT': '5432',          # PostgreSQL 기본 포트
    }
}
