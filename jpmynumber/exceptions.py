# -*- coding:utf-8 -*-


class JPMyNumberError(ValueError):
    pass


class JPMyNumberValueError(JPMyNumberError):
    pass


class JPMyNumberLengthError(JPMyNumberError):
    pass


class JPMyNumberCheckDigitError(JPMyNumberError):
    pass


class JPMyNumberPatternError(JPMyNumberError):
    pass
