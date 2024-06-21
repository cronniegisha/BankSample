from rest_framework import serializers
from .models import Account, Transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id', 'account_number', 'owner', 'balance']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'account', 'amount', 'timestamp', 'transaction_type']
