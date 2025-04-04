from .base import *

DEBUG = True

ALLOWED_HOSTS = []

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
