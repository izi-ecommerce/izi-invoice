import factory

from izi.core.loading import get_model

__all__ = ['LegalEntityAddressFactory', 'LegalEntityFactory']


class LegalEntityFactory(factory.DjangoModelFactory):
    business_name = 'Test Company'
    vat_number = 'test-vat-number'

    class Meta:
        model = get_model('izi_invoices', 'LegalEntity')


class LegalEntityAddressFactory(factory.DjangoModelFactory):
    legal_entity = factory.SubFactory(LegalEntityFactory)
    line1 = '1 Egg Street'
    line2 = 'London'
    postcode = 'N12 9RE'
    country = factory.SubFactory('izi.test.factories.CountryFactory')

    class Meta:
        model = get_model('izi_invoices', 'LegalEntityAddress')
