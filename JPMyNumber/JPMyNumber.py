# -*- coding:utf-8 -*-


class _ValidatorMixin(object):

    def validate_length(self):
        return len(self._to_s) == self.LEN

    def validate_check_digit(self):
        return self.true_check_digit == self.check_digit


class JPMyNumber(_ValidatorMixin):

    LEN = 12

    def __init__(self, number):
        self.number = int(number)

    @property
    def check_digit(self):
        return self._to_l[-1]

    @property
    def true_check_digit(self):
        user_number_len = len(self._user_number_to_l)
        temp = sum([self._f(n) for n in range(1, self.LEN)]) % user_number_len
        if temp <= 1:
            return 0
        return user_number_len - temp

    @property
    def _to_l(self):
        return [int(s) for s in self._to_s]

    @property
    def _to_s(self):
        return str(self.number)

    @property
    def _user_number_to_l(self):
        return self._to_l[0: -1]

    def _p(self, n):
        return self._user_number_to_l[-n]

    def _q(self, n):
        if 1 <= n <= (self.LEN / 2):
            return n + 1
        if (self.LEN / 2) < n <= len(self._user_number_to_l):
            return n - 5
        raise

    def _f(self, n):
        return self._p(n) * self._q(n)
