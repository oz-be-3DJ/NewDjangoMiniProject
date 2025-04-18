from django.urls import path
from account.views import AccountList

urlpatterns = [
   path('', AccountList.as_view(), name='account_info_list')
]
