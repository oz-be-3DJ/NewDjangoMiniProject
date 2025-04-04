from rest_framework import serializers

from apps.account.models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__' # 모든 필드 가져오기
        read_only_fields = ('id', 'account_number', 'account_type', 'bank_code', 'user')