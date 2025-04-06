from .base import *

from dotenv import load_dotenv
load_dotenv(BASE_DIR / '.env')  # .env 파일 로드
# print("S3_REGION_NAME:", os.getenv("S3_REGION_NAME"))

DEBUG = True

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "15.164.244.79",  # EC2 퍼블릭 IP
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv("DB_NAME"),              # 생성한 DB 이름
        'USER': os.getenv("DB_USER"),              # PostgreSQL 사용자
        'PASSWORD': os.getenv("DB_PASSWORD"),      # 비밀번호
        'HOST': os.getenv("DB_HOST"),              # 로컬에서 실행 중이므로 localhost
        'PORT': os.getenv("DB_PORT", "5432"),      # RDS 엔드포인트
    }
}

# Static, Media URL 수정
STATIC_URL = f'https://{os.getenv("S3_STORAGE_BUCKET_NAME", "django-mini-project")}.s3.amazonaws.com/static/'
MEDIA_URL = f'https://{os.getenv("S3_STORAGE_BUCKET_NAME", "django-mini-project")}.s3.amazonaws.com/media/'

# STORAGES 작성
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": os.getenv("S3_ACCESS_KEY", ""),
            "secret_key": os.getenv("S3_SECRET_ACCESS_KEY", ""),
            "bucket_name": os.getenv("S3_STORAGE_BUCKET_NAME", ""),
            "region_name": os.getenv("S3_REGION_NAME", ""),
            "location": "media",
            "default_acl": "public-read",
        },
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
        "OPTIONS": {
            "access_key": os.getenv("S3_ACCESS_KEY", ""),
            "secret_key": os.getenv("S3_SECRET_ACCESS_KEY", ""),
            "bucket_name": os.getenv("S3_STORAGE_BUCKET_NAME", ""),
            "region_name": os.getenv("S3_REGION_NAME", ""),
            "custom_domain": f'{os.getenv("S3_STORAGE_BUCKET_NAME", "")}.s3.amazonaws.com',
            "location": "static",
            "default_acl": "public-read",
        },
    },
}
