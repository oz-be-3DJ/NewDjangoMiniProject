from django.urls import path
from apps.transaction.views import CreateTransactionView, TransactionDetailView

urlpatterns = [
    path('', CreateTransactionView.as_view(), name='create_transaction'),
    path('<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
]