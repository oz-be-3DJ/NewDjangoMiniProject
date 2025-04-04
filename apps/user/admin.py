from django.contrib import admin

from apps.user.models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','email','nickname', 'name', 'phone_number','is_active', 'is_staff', 'is_admin', 'last_login', 'created_at', 'updated_at') # 관리자 목록 페이지에 보여줄 컬럼
    list_filter = ('is_active', 'is_staff', 'is_admin',)  # 필터 사이드바에 표시할 필드
    search_fields = ('email','nickname', 'name', 'phone_number')  # 검색창을 통해 검색할 수 있는 필드
    ordering = ('-created_at',)  # 생성일 기준으로 최신순 정렬
    list_display_links = ('email','nickname', 'name')  # 목록에서 content를 클릭하면 상세 페이지로 이동
    fieldsets = (
        ('기본 정보', {
            'fields': ('email', 'nickname', 'name', 'phone_number')
        }),
        ('권한', {
            'fields': ('is_active', 'is_staff', 'is_admin')
        }),
    )