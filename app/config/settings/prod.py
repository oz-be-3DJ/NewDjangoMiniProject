from .base import *

from dotenv import load_dotenv
load_dotenv(BASE_DIR.parent / '.env')  # .env 파일 로드
# print("S3_REGION_NAME:", os.getenv("S3_REGION_NAME"))

# DEBUG = True
DEBUG = False

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
print(STATIC_URL)


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

# # Email
# # from django.core.mail.backends.smtp import EmailBackend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.naver.com' # 네이버 환결설정에서 볼 수 있음.
EMAIL_USE_TLS = True  # 보안연결
EMAIL_PORT = 587  # 네이버 메일 환경설정에서 확인 가능
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD =  os.getenv("EMAIL_HOST_PASSWORD", "")
