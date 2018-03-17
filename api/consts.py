# coding: utf-8
from __future__ import unicode_literals

FOOD_PRICE = 4.0
SHOWER_PRICE = 2.0
MAX_SHIT_NUM = 12
CREATE_SHIT_PERIOD = 5 * 60


class ChoiceBase(object):
    __choices__ = ()

    def get_choices(self):
        return self.__choices__

    @classmethod
    def get_display_name(cls, value):
        _names = dict(cls.__choices__)
        return _names.get(value) or ""

    @classmethod
    def all_elements(cls):
        _dict = dict(cls.__choices__)
        return _dict.keys()


class CharacterType(ChoiceBase):
    elegant = 1
    sexy = 2
    lively = 3
    intelligent = 4
    cool = 5
    gentle = 6
    nice = 7
    sunup = 8

    __choices__ = (
        (elegant, '温柔优雅'),
        (sexy, '火辣性感'),
        (lively, '活泼可爱'),
        (intelligent, '常熟知性'),
        (cool, '疯狂炫酷'),
        (gentle, '儒雅绅士'),
        (nice, '温柔体贴'),
        (sunup, '阳光向上')
    )


class DogType(ChoiceBase):
    shapi = 1
    samoye = 2
    jinmao = 3
    dimu = 4

    __choices__ = (
        (shapi, '沙皮'),
        (samoye, '萨摩'),
        (jinmao, '金毛'),
        (dimu, '蒂姆')
    )
