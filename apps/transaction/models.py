from django.db import models

from apps.account.models import Account


# Create your models here.
class TransactionHistory(models.Model):
    # TransactionHistory ID (Primary Key)
    # id = models.AutoField(
    #     primary_key=True,
    #     verbose_name = "거래내역 ID",
    # )

    # 계좌 ID (Foreign Key)
    account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        verbose_name="계좌 ID",
    )

    # 거래 금액
    transaction_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="거래 금액",
    )

    # 거래 후 잔액
    balance_after = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        verbose_name="거래 후 잔액",
    )

    # 거래 인자 내역
    transaction_detail = models.CharField(
        max_length=30,
        verbose_name="계좌 입/출 내역",
    )

    # 입출금 타입 (ENUM)
    TRANSACTION_TYPE_CHOICES = [
        ('입금', '입금'),
        ('출금', '출금'),
    ]
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
        verbose_name="입출금 타입",
    )

    # 결제 타입 (ENUM)
    PAYMENT_TYPE_CHOICES = [
        ('현금', '현금'),
        ('카드', '카드'),
        ('계좌이체', '계좌이체'),
        ('자동이체', '자동이체'),
    ]
    payment_type = models.CharField(
        max_length=20,
        choices=PAYMENT_TYPE_CHOICES,
        verbose_name="결제 타입"
    )

    # 거래일
    transaction_data = models.DateTimeField(
        auto_now_add=True,
        verbose_name="거래 일시",
    )

    class Meta:
        db_table = 'transaction_history'
        verbose_name = '결제 내역'
        verbose_name_plural = '결제 내역 목록'