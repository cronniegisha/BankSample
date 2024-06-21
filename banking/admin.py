from django.contrib import admin

from django.contrib import admin
from .models import Account, Transaction

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'owner', 'balance')
    search_fields = ('account_number', 'owner')

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('account', 'amount', 'transaction_type', 'timestamp')
    list_filter = ('transaction_type', 'timestamp')
    search_fields = ('account__account_number', 'account__owner')

admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)

