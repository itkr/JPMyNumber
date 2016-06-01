# -*- coding:utf-8 -*-
import random

from jpmynumber.exceptions import (JPMyNumberCheckDigitError,
                                   JPMyNumberLengthError,
                                   JPMyNumberPatternError,
                                   JPMyNumberValueError)


def assert_n(func):
    def validate(self, n):
        assert 1 <= n < self.LEN
        return func(self, n)
    return validate


class Pattern(list):

    def copy(self):
        return Pattern([i for i in self])

    def check(self, index, n):
        if self[index] is None:
            return True
        if hasattr(self[index], '__iter__'):
            return n in self[index]
        return n == self[index]

    def update(self, index, n):
        self[index] = n
        return self


class _ValidationMixin(object):

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

    def validate_pattern(self):
        if not self.check_pattern(self.pattern):
            raise JPMyNumberPatternError

    def validate(self):
        self.validate_digit()
        self.validate_length()
        self.validate_pattern()
        self.validate_check_digit()


class _CreationMixin(object):

    @classmethod
    def random_create(cls):
        start = int('1' + '0' * (cls.LEN - 1))
        stop = int('9' * cls.LEN)
        obj = cls(random.randint(start, stop), False)
        obj._update_pattern()
        obj._update_check_digit()
        obj.validate()
        return obj

    def _update_check_digit(self):
        arr = self._to_a
        arr[self._check_digit_index] = self.true_check_digit
        self.number = int(''.join([str(i) for i in arr]))

    def _update_pattern(self):
        arr = self._to_a
        for i, pattern_n in enumerate(self.pattern):
            if pattern_n is not None:
                arr[i] = random.choice(pattern_n) if hasattr(
                    pattern_n, '__iter__') else pattern_n
        self.number = int(''.join([str(i) for i in arr]))


class JPMyNumber(_CreationMixin, _ValidationMixin):

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
    def pattern(self):
        return Pattern([None for _i in range(self.LEN)])

    @property
    def check_digit(self):
        return self._to_a[self._check_digit_index]

    @property
    def true_check_digit(self):
        user_number_len = len(self._user_number_to_a)
        remainder = sum([self._f(n)
                         for n in range(1, self.LEN)]) % user_number_len
        return 0 if remainder <= 1 else user_number_len - remainder

    @property
    def _check_digit_index(self):
        return self.LEN - 1

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
        arr = [i for i in self._to_a]
        del arr[self._check_digit_index]
        return arr

    @assert_n
    def _p(self, n):
        return self._user_number_to_a[-n]

    @assert_n
    def _q(self, n):
        return n + 1 if n <= (self.LEN / 2) else n - 5

    @assert_n
    def _f(self, n):
        return self._p(n) * self._q(n)

    def check_pattern(self, pattern):
        for i, n in enumerate(self._to_a):
            if not pattern.check(i, n):
                return False
        return True
