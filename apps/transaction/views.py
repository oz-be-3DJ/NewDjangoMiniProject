from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Account,TransactionHistory
from .serializers import TransactionHistorySerializer


# Create your views here.
class CreateTransactionView(APIView):
    def post(self, request):
        # Serializer를 사용해 요청 데이터 검증
        serializer = TransactionHistorySerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data

        # 계좌 확인 (없으면 404 에러)
        try:
            account = data['account']
        except Account.DoesNotExist:
            return Response({"error": "계좌를 찾을 수 없습니다."}, status=status.HTTP_404_NOT_FOUND)

        # 계좌의 금액이 출금 금액보다 적을 경우 (400 에러)
        if data['transaction_type'] == '출금' and account.balance < data['transaction_amount']:
            return Response({"error": "잔액 부족"}, status=status.HTTP_400_BAD_REQUEST)

        if data['transaction_type'] == '입금':  # 거래 유형이 '입금'이면
            balance_after = account.balance + data['transaction_amount']  # 현재 잔액에 거래 금액을 더함
        else:  # 거래 유형이 '입금'이 아니면
            balance_after = account.balance - data['transaction_amount']  # 현재 잔액에서 거래 금액을 뺌

        # 거래 내역 생성
        transaction = TransactionHistory.objects.create(
            account=account, # 계좌
            transaction_amount=data['transaction_amount'], # 거래 금액
            balance_after=balance_after, # 거래 후 잔액(자동 계산)
            transaction_detail=data['transaction_detail'], # 거래 인자 내역
            transaction_type=data['transaction_type'], # 입출금 타입
            payment_type=data['payment_type'] # 결제 타입
        )

        # 계좌 잔액 업데이트
        account.balance = balance_after
        account.save()

        response_serializer = TransactionHistorySerializer(transaction)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)