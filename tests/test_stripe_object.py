"""
.. module:: dj-stripe.tests.test_stripe_object
   :synopsis: dj-stripe StripeObject Model Tests.

.. moduleauthor:: Bill Huneke (@wahuneke)

"""
from django.test import TestCase

from djstripe.fields import StripeCharField
from djstripe.models import StripeObject


SIMPLE_OBJ = {
    'id': 'yo',
    'livemode': True
}
SIMPLE_OBJ_RESULT = {
    'id': 'yo',
    'description': None,
    'livemode': True,
    'metadata': None,
    'created': None
}


class StripeObjectExceptionsTest(TestCase):
    def test_missing_required_field(self):
        class HasRequiredField(StripeObject):
            im_not_optional = StripeCharField()

    def test_missing_nonrequired_field(self):
        class HasNotRequiredField(StripeObject):
            im_not_optional = StripeCharField(stripe_required=False)

        # Should be no exception here
        obj = HasNotRequiredField._stripe_object_to_record(SIMPLE_OBJ)
        self.assertEqual(obj['im_not_optional'], None)


class StripeObjectBasicTest(TestCase):
    def test_basic_val_to_db(self):
        # Instantiate a stripeobject model class
        class BasicModel(StripeObject):
            pass

        result = BasicModel._stripe_object_to_record(SIMPLE_OBJ)
        self.assertEqual(result, SIMPLE_OBJ_RESULT)
