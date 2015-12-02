# -*- coding:utf-8 -*-
import random

from jpmynumber.exceptions import (JPMyNumberCheckDigitError,
                                   JPMyNumberLengthError, JPMyNumberValueError)


def _assert_n(func):
    def validate(self, n):
        assert 1 <= n < self.LEN
        return func(self, n)
    return validate


class _ValidatorMixin(object):

    def validate_digit(self):
        try:
            int(self.number)
        except ValueError:
            raise JPMyNumberValueError

    def validate_length(self):
        if not len(self._to_s) == self.LEN:
            raise JPMyNumberLengthError

    def validate_check_digit(self):
        if not self.true_check_digit == self.check_digit:
            raise JPMyNumberCheckDigitError

    def validate(self):
        self.validate_digit()
        self.validate_length()
        self.validate_check_digit()


class _CreateMixin(object):

    @classmethod
    def random_create(cls):
        obj = cls(
            random.randint(int('1' + '0' * (cls.LEN - 1)), int('9' * cls.LEN)),
            False)
        obj._update_check_digit()
        return obj


class JPMyNumber(_CreateMixin, _ValidatorMixin):

    LEN = 12

    def __init__(self, number, validation=True):
        self.number = str(number)
        if validation:
            self.validate()

    def __repr__(self):
        return '<{module}.{_class}(\'{number}\')>'.format(
            module=self.__module__,
            _class=self.__class__.__name__,
            number=self.number)

    @property
    def check_digit(self):
        return self._to_a[-1]

    @property
    def true_check_digit(self):
        user_number_len = len(self._user_number_to_a)
        remainder = sum([self._f(n)
                         for n in range(1, self.LEN)]) % user_number_len
        return 0 if remainder <= 1 else user_number_len - remainder

    @property
    def _to_a(self):
        return [int(s) for s in self._to_s]

    @property
    def _to_s(self):
        return str(self.number)

    @property
    def _to_i(self):
        return int(self.number, 10)

    @property
    def _user_number_to_a(self):
        return self._to_a[0: -1]

    @_assert_n
    def _p(self, n):
        return self._user_number_to_a[-n]

    @_assert_n
    def _q(self, n):
        return n + 1 if n <= (self.LEN / 2) else n - 5

    @_assert_n
    def _f(self, n):
        return self._p(n) * self._q(n)

    def _update_check_digit(self):
        number_list = self._user_number_to_a + [self.true_check_digit]
        self.number = int(''.join([str(i) for i in number_list]))


class CorporationMyNumber(JPMyNumber):

    LEN = 13

    @property
    def _user_number_to_a(self):
        return self._to_a[1:]

    @_assert_n
    def _q(self, n):
        return 1 if n % 2 else 2

    @property
    def check_digit(self):
        return self._to_a[0]

    @property
    def true_check_digit(self):
        return 9 - sum([self._f(n) for n in range(1, self.LEN)]) % 9

    def _update_check_digit(self):
        number_list = [self.true_check_digit] + self._user_number_to_a
        self.number = int(''.join([str(i) for i in number_list]))
