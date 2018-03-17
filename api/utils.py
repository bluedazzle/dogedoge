# coding: utf-8
from __future__ import unicode_literals


def deduction(user, price):
    if user.money < price:
        return False
    user.money -= price
    return True
