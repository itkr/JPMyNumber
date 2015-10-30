# -*- coding:utf-8 -*-
import random

from jpmynumber.exceptions import (JPMyNumberCheckDigitError,
                                   JPMyNumberLengthError)


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


class _CreateMixin(object):

    @classmethod
    def random_create(cls):
        temp = cls(
            random.randint(int('1' + '0' * (cls.LEN - 1)), int('9' * cls.LEN)),
            False)
        number_list = temp._user_number_to_a + [temp.true_check_digit]
        return cls(int(''.join([str(i) for i in number_list])))


class JPMyNumber(_CreateMixin, _ValidatorMixin):

    LEN = 12

    def __init__(self, number, validation=True):
        self.number = int(number)
        if validation:
            self.validate()

    def __repr__(self):
        return '<{module}.{_class}({number})>'.format(
            module=self.__module__,
            _class=self.__class__.__name__,
            number=self.number)

    @property
    def check_digit(self):
        return self._to_a[-1]

    @property
    def true_check_digit(self):
        user_number_len = len(self._user_number_to_a)
        temp = sum([self._f(n) for n in range(1, self.LEN)]) % user_number_len
        if temp <= 1:
            return 0
        return user_number_len - temp

    @property
    def _to_a(self):
        return [int(s) for s in self._to_s]

    @property
    def _to_s(self):
        return str(self.number)

    @property
    def _user_number_to_a(self):
        return self._to_a[0: -1]

    def _p(self, n):
        return self._user_number_to_a[-n]

    def _q(self, n):
        if 1 <= n <= (self.LEN / 2):
            return n + 1
        if (self.LEN / 2) < n <= len(self._user_number_to_a):
            return n - 5
        raise

    def _f(self, n):
        return self._p(n) * self._q(n)
