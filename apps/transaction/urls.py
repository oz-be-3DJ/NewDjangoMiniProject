from django.urls import path
from apps.transaction.views import CreateTransactionView

urlpatterns = [
    path('', CreateTransactionView.as_view(), name='create_transaction'),
]