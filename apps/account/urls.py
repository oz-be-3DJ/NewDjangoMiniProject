from django.urls import path
from apps.account.views import AccountList

urlpatterns = [
   path('', AccountList.as_view(), name='account_info_list')
]
