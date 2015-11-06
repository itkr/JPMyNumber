# -*- coding:utf-8 -*-

from .core import JPMyNumber, _assert_n


class LegalEntityNumber(JPMyNumber):

    LEN = 13

    @property
    def _check_digit_index(self):
        return 0

    @_assert_n
    def _q(self, n):
        return 1 if n % 2 else 2

    @property
    def true_check_digit(self):
        return 9 - sum([self._f(n) for n in range(1, self.LEN)]) % 9


class StateOrgansNumber(LegalEntityNumber):

    """C00001XXXXXXX　国家機関."""

    def get_pattern(self):
        pattern = super(StateOrgansNumber, self).get_pattern()
        pattern[1] = 0
        pattern[2] = 0
        pattern[3] = 0
        pattern[4] = 0
        pattern[5] = 1
        return pattern


class LocalGovernmentNumber(LegalEntityNumber):

    """C0000[2-3]XXXXXXX　地方公共団体."""

    def get_pattern(self):
        pattern = super(LocalGovernmentNumber, self).get_pattern()
        pattern[1] = 0
        pattern[2] = 0
        pattern[3] = 0
        pattern[4] = 0
        pattern[5] = [2, 3]
        return pattern


class LocalGovernmentNumberWithCode(LocalGovernmentNumber):

    """C00002XXXXXXX　地方公共団体（団体コードあり）."""

    def get_pattern(self):
        pattern = super(LocalGovernmentNumberWithCode, self).get_pattern()
        pattern[5] = 2
        return pattern


class LocalGovernmentNumberWithoutCode(LocalGovernmentNumber):

    """C00003XXXXXXX　地方公共団体（団体コードなし）."""

    def get_pattern(self):
        pattern = super(LocalGovernmentNumberWithoutCode, self).get_pattern()
        pattern[5] = 3
        return pattern


class CorporationNumber(LegalEntityNumber):

    """CXXXXXXXXXXXX　会社法人等."""
    pass


class OtherOrganizationNumber(LegalEntityNumber):

    """C7001XXXXXXXX　人格の無い団体等."""

    def get_pattern(self):
        pattern = super(OtherOrganizationNumber, self).get_pattern()
        pattern[1] = 7
        pattern[2] = 0
        pattern[3] = 0
        pattern[4] = 1
        return pattern
