from django.db import models

# Create your models here.
from django.db import models

class BankCode(models.Model):
    # id = models.AutoField(primary_key=True)
    code = models.CharField(primary_key=True, max_length=20, verbose_name="은행 코드")
    name = models.CharField(max_length=15, unique=True, verbose_name="은행 이름")

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        db_table = 'bank_code'
        verbose_name = '은행 코드'
        verbose_name_plural = '은행 코드 목록'
