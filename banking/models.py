from django.db import models

from django.db import models

class Account(models.Model):
    account_number = models.CharField(max_length=20, unique=True)
    owner = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.owner} - {self.account_number}"

class Transaction(models.Model):
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal')
    )
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f"{self.account} - {self.transaction_type} - {self.amount}"

