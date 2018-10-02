from django.conf import settings

IZI_INVOICES_DOCUMENTS_ROOT = getattr(settings, 'IZI_INVOICES_DOCUMENTS_ROOT', 'documents/')

IZI_INVOICES_UPLOAD_FOLDER = getattr(settings, 'IZI_INVOICES_UPLOAD_FOLDER', 'invoices/%Y/%m/')

IZI_INVOICES_INVOICE_MODEL = getattr(settings, 'IZI_INVOICES_INVOICE_MODEL', 'izi_invoices.Invoice')
