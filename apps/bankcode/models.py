from django.db import models

# Create your models here.
from django.db import models

class BankCode(models.Model):
    bank_id = models.AutoField(primary_key=True)
    bank_code = models.CharField(max_length=20, unique=True, verbose_name="은행 코드")
    bank_name = models.CharField(max_length=15, unique=True, verbose_name="은행 이름")

    def __str__(self):
        return f"{self.bank_name} ({self.bank_code})"