from django.db import models

# Create your models here.
class TransactionHistory(models.Model):
    # TransactionHistory ID (Primary Key)
    id = models.AutoField(primary_key=True)

    # 계좌 ID (Foreign Key)
    # account_id = models.ForeignKey(
    #     'apps.account.Account',
    #     on_delete=models.CASCADE,
    # ) marge 후 주석 풀기

    # 거래 금액
    transaction_amount = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    # 거래 후 잔액
    balance_after = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    # 거래 인자 내역
    transaction_detail = models.CharField(
        max_length=30,
    )

    # 입출금 타입 (ENUM)
    TRANSACTION_TYPE_CHOICES = [
        ('입금', '입금'),
        ('출금', '출금'),
    ]
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPE_CHOICES,
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
    )

    class Meta:
        db_table = 'transaction_history'
        verbose_name = '결제 내역'
        verbose_name_plural = '결제 내역 목록'