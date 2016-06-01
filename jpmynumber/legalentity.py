# -*- coding:utf-8 -*-

from .core import JPMyNumber, assert_n


class LegalEntityNumber(JPMyNumber):

    LEN = 13

    @property
    def true_check_digit(self):
        return 9 - sum([self._f(n) for n in range(1, self.LEN)]) % 9

    @property
    def _check_digit_index(self):
        return 0

    @assert_n
    def _q(self, n):
        return n % 2 or 2


class StateOrgansNumber(LegalEntityNumber):

    """C00001XXXXXXX　国家機関."""

    @property
    def pattern(self):
        pattern = super(StateOrgansNumber, self).pattern.copy()
        pattern.update(1, 0)
        pattern.update(2, 0)
        pattern.update(3, 0)
        pattern.update(4, 0)
        pattern.update(5, 1)
        return pattern


class LocalGovernmentNumber(LegalEntityNumber):

    """C0000[2-3]XXXXXXX　地方公共団体."""

    @property
    def pattern(self):
        pattern = super(LocalGovernmentNumber, self).pattern.copy()
        pattern.update(1, 0)
        pattern.update(2, 0)
        pattern.update(3, 0)
        pattern.update(4, 0)
        pattern.update(5, [2, 3])
        return pattern


class LocalGovernmentNumberWithCode(LocalGovernmentNumber):

    """C00002XXXXXXX　地方公共団体（団体コードあり）."""

    @property
    def pattern(self):
        pattern = super(LocalGovernmentNumberWithCode, self).pattern.copy()
        return pattern.update(5, 2)


class LocalGovernmentNumberWithoutCode(LocalGovernmentNumber):

    """C00003XXXXXXX　地方公共団体（団体コードなし）."""

    @property
    def pattern(self):
        pattern = super(LocalGovernmentNumberWithoutCode, self).pattern.copy()
        return pattern.update(5, 3)


class CorporationNumber(LegalEntityNumber):

    """CXXXXXXXXXXXX　会社法人等."""
    pass


class OtherOrganizationNumber(LegalEntityNumber):

    """C7001XXXXXXXX　人格の無い団体等."""

    @property
    def pattern(self):
        pattern = super(OtherOrganizationNumber, self).pattern.copy()
        pattern.update(1, 7)
        pattern.update(2, 0)
        pattern.update(3, 0)
        pattern.update(4, 1)
        return pattern
