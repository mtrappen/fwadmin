import unittest
from django.core.exceptions import ValidationError
from fwadmin.validators import validate_port


class ValidatorTests(unittest.TestCase):
    """ Unit tests for validator.py """

    def test_validate_port(self):
        # expected to be valid
        valid = (
            '10-20', '1-65535',
            '33', '44', '1024', '5000',
            ' 42     ', '    42', '1     - 5',
            '11-11',

        )
        # expected to raise ValidationError
        invalid = (
            '17-', '-6',
            '300000000000', '1-9000000000000',
            '1337-42',
            '14,15,16', '10 10 10',
            '', '-',
            'spam', '1-spam', 'spam-10', 'spam-spam',
            '1-2-3', '1--2', '-1-100'
        )
        for case in valid:
            self.assertEqual(validate_port(case), None)
        for case in invalid:
            with self.assertRaises(ValidationError):
                validate_port(case)