from django.db import models

from django.db import models
#from django.contrib.auth.models import User

class Account(models.Model):
    id = models.AutoField(primary_key=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE) # 유저와 테이블
    #bank = models.ForeignKey(Bank, on_delete=models.CASCADE) # 은행 코드 (은행은 여러 개의 계좌를 가질 수 있음)
    account_number = models.CharField(max_length=20) # 계좌 번호
    account_type = models.CharField(max_length=15) # 계좌 종류 (입출금, 저축, 예금 등)
    balance = models.DecimalField(max_digits=12, decimal_places=2) # 계좌 잔액
    created_at = models.DateTimeField(auto_now_add=True) # 계좌 생성일 (객체 생성 때 자동으로 설정)
    updated_at = models.DateTimeField(auto_now=True) # 계좌 수정일 (객체가 수정될 때 자동으로 설정)

    def __str__(self):
        return f"ID: {self.id}, 계좌번호: {self.account_number}, 종류: {self.account_type}, 잔액: {self.balance}"

