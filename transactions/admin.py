from django.contrib import admin
from .models import Transaction


class TransactionAdmin(admin.ModelAdmin):
    # Specify the fields to display
    list_display = ('id', 'date', 'description', 'amount')


admin.site.register(Transaction, TransactionAdmin)
