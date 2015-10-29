# -*- coding:utf-8 -*-
from .exceptions import JPMyNumberCheckDigitError, JPMyNumberLengthError


class _ValidatorMixin(object):

    def validate_length(self):
        if not len(self._to_s) == self.LEN:
            raise JPMyNumberLengthError

    def validate_check_digit(self):
        if not self.true_check_digit == self.check_digit:
            raise JPMyNumberCheckDigitError

    def validate(self):
        self.validate_length()
        self.validate_check_digit()
