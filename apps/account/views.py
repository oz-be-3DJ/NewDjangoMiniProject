from django.shortcuts import render
from rest_framework.generics import ListAPIView
from apps.account.models import Account
from apps.account.serializers import AccountSerializer


class AccountList(ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer