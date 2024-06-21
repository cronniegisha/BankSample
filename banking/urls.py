from django.urls import path
from .views import AccountListCreateView, AccountDetailView, TransactionListCreateView, deposit, withdraw

urlpatterns = [
    path('', AccountListCreateView.as_view(), name='account-list-create'),
    path('accounts/', AccountListCreateView.as_view(), name='account-list-create'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account-detail'),
    path('accounts/<int:pk>/deposit/', deposit, name='account-deposit'),
    path('accounts/<int:pk>/withdraw/', withdraw, name='account-withdraw'),
    path('transactions/', TransactionListCreateView.as_view(), name='transaction-list-create'),
    path('transactions/<int:pk>/', TransactionListCreateView.as_view(), name='transaction-detail'),
]
