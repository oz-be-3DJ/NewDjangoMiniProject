from django.shortcuts import render
from rest_framework.generics import ListAPIView
from account.models import Account
from account.serializers import AccountSerializer


class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer