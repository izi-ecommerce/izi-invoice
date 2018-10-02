# Generated by Django 2.0.8 on 2018-08-22 13:35

from django.db import migrations, models
import izi_invoices.storages


class Migration(migrations.Migration):

    dependencies = [
        ('izi_invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='document',
            field=models.FileField(blank=True, max_length=255, null=True, storage=izi_invoices.storages.DocumentsStorage(), upload_to='invoices/%Y/%m/', verbose_name='Document'),
        ),
    ]
