# -*- coding:utf-8 -*-
import random


class _CreateMixin(object):

    @classmethod
    def random_create(cls):
        temp = cls(
            random.randint(int('1' + '0' * (cls.LEN - 1)), int('9' * cls.LEN)),
            False)
        number_list = temp._user_number_to_a + [temp.true_check_digit]
        return cls(int(''.join([str(i) for i in number_list])))
