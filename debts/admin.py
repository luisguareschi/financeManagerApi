from django.contrib import admin

# Register your models here.

from .models import Debt, Debtor


@admin.register(Debtor)
class DebtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_by')
    search_fields = ('name', 'created_by__username')
    readonly_fields = (
        'id',
    )


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'amount', 'user', 'created')
    search_fields = ('description', 'user__username')
    list_filter = ('user',)
    readonly_fields = (
        'id',
        'created',
        'modified',
    )
