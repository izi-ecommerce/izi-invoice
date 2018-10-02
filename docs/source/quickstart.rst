Quickstart
==========

Installation
------------

.. code-block:: console

    $ pip install django-izi-invoices


Setup
=====

1. Add ``izi_invoices`` to the ``INSTALLED_APPS`` variable of your
   project's ``settings.py``.

2. Sync the database using ``python manage.py migrate``.

3. Create instances of ``LegalEntity`` and ``LegalEntityAddress``.

4. Integrate ``InvoiceCreator`` in your checkout process.
