from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Account, Transaction
from .serializers import AccountSerializer, TransactionSerializer

# Class-based views for Account
class AccountListCreateView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

# Function-based views for deposit and withdraw
@api_view(['POST'])
def deposit(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    amount = request.data.get('amount')
    if amount:
        account.balance += float(amount)
        account.save()
        Transaction.objects.create(account=account, amount=amount, transaction_type='deposit')
        return Response({'status': 'deposit successful'})
    return Response({'status': 'amount required'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def withdraw(request, pk):
    try:
        account = Account.objects.get(pk=pk)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    amount = request.data.get('amount')
    if amount:
        if account.balance >= float(amount):
            account.balance -= float(amount)
            account.save()
            Transaction.objects.create(account=account, amount=amount, transaction_type='withdrawal')
            return Response({'status': 'withdrawal successful'})
        return Response({'status': 'insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'status': 'amount required'}, status=status.HTTP_400_BAD_REQUEST)

# Class-based views for Transaction
class TransactionListCreateView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

