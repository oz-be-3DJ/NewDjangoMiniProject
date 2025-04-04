from rest_framework import serializers

from apps.transaction.models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = "__all__"
        read_only_fields = ["id", "balance_after"]

    def validate_transaction_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("거래 금액은 0보다 커야 합니다.")
        return value

    def validate_transaction_type(self, value):
        if value not in ['입금', '출금']:
            raise serializers.ValidationError("유효하지 않은 거래 유형입니다. '입금' 또는 '출금'만 가능합니다.")
        return value

    def validate_payment_type(self, value):
        if value not in ['현금', '카드', '계좌이체', '자동이체']:
            raise serializers.ValidationError("유효하지 않은 결제 방식입니다. '현금', '카드', '계좌이체', '자동이체'만 가능합니다.")
        return value