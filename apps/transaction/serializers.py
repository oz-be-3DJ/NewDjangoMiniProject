from rest_framework import serializers

from apps.transaction.models import TransactionHistory


class TransactionHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionHistory
        fields = "__all__"
        read_only_fields = ["id"]