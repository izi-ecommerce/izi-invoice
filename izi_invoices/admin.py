from django.contrib import admin

from izi.core.loading import get_model

from .models import is_custom_invoice_model

LegalEntity = get_model('izi_invoices', 'LegalEntity')
LegalEntityAddress = get_model('izi_invoices', 'LegalEntityAddress')

admin.site.register(LegalEntity)
admin.site.register(LegalEntityAddress)

if not is_custom_invoice_model:
    Invoice = get_model('izi_invoices', 'Invoice')
    admin.site.register(Invoice)
