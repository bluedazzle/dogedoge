# coding: utf-8
from __future__ import unicode_literals

import random
import string

import datetime

from django.utils.timezone import get_current_timezone
from django.views.generic import DetailView
from django.views.generic import ListView

from api.consts import FOOD_PRICE, SHOWER_PRICE, MAX_SHIT_NUM, CREATE_SHIT_PERIOD
from api.utils import deduction
from core.Mixin.CheckMixin import CheckSecurityMixin, CheckTokenMixin
from core.Mixin.JsonRequestMixin import JsonRequestMixin
from core.Mixin.StatusWrapMixin import StatusWrapMixin
from core.dss.Mixin import MultipleJsonResponseMixin, JsonResponseMixin
from core.models import Goods, TTUser, Pet, Gift, PetShip
import core.Mixin.StatusWrapMixin as SW


class GoodsListView(CheckTokenMixin, StatusWrapMixin, MultipleJsonResponseMixin, ListView):
    """
    商品列表
    """
    model = Goods
    include_attr = ['id', 'name', 'price', 'picture']
    paginate_by = 20
    http_method_names = ['get', 'post']


class GoodsView(CheckTokenMixin, StatusWrapMixin, JsonResponseMixin, DetailView):
    """
    商品购买
    """
    model = Goods
    pk_url_kwarg = 'gid'
    http_method_names = ['post', 'get']
    include_attr = ['money', 'nick']

    def post(self, request, *args, **kwargs):
        if not self.wrap_check_token_result():
            return self.render_to_response({})
        goods = self.get_object()
        if self.user.money < goods.price:
            self.message = '余额不足'
            self.status_code = SW.ERROR_DATA
            return self.render_to_response({})
        self.user.money = self.user.money - goods.price
        Gift(name=goods.name, picture=goods.picture, belong=self.user, goods=goods).save()
        self.user.save()
        return self.render_to_response({'user': self.user})


class PetUserInfo(CheckTokenMixin, StatusWrapMixin, JsonResponseMixin, DetailView):
    """
    获取宠物|新建宠物信息
    """
    model = Pet
    include_attr = ['user_id', 'nick', 'male', 'avatar', 'city', 'country', 'province', 'name', 'type', 'sex',
                    'character', 'wish', 'picture', 'showerd', 'eated', 'belong', 'money', 'pick']
    foreign = True
    http_method_names = ['get', 'post']

    def get_object(self, queryset=None):
        pets = Pet.objects.filter(belong=self.user)
        if pets.exists():
            return pets[0]
        self.message = '宠物不存在'
        self.status_code = SW.INFO_NO_EXIST
        return False

    def calculate_shit(self):
        if self.user.pick >= MAX_SHIT_NUM:
            return True
        now = datetime.datetime.now(tz=get_current_timezone())
        period = now - self.user.last_pick_time
        p_num = period.seconds / CREATE_SHIT_PERIOD
        if not p_num:
            return True
        exist_num = self.user.pick
        p_num += exist_num
        self.user.last_pick_time = now
        self.user.pick = p_num if p_num <= MAX_SHIT_NUM else MAX_SHIT_NUM
        self.user.save()
        return True

    def get(self, request, *args, **kwargs):
        super(PetUserInfo, self).get(request, *args, **kwargs)
        pet = self.get_object()
        if not pet:
            return self.render_to_response({})
        self.calculate_shit()
        return self.render_to_response({'pet': pet})

    def post(self, request, *args, **kwargs):
        if not self.wrap_check_token_result():
            return self.render_to_response({})
        pet = self.get_object()
        if pet:
            self.message = '宠物已存在'
            self.status_code = SW.INFO_EXISTED
            return self.render_to_response({})
        self.message = 'success'
        self.status_code = SW.INFO_SUCCESS
        pet_type = request.POST.get('type')
        sex = request.POST.get('sex')
        character = request.POST.get('character')
        wish = request.POST.get('wish')
        pet = Pet()
        pet.name = '{0}的狗子'.format(self.user.nick)
        pet.sex = sex
        pet.character = character
        pet.wish = wish
        pet.type = pet_type
        pet.belong = self.user
        pet.save()
        return self.render_to_response({'pet': pet})


class UserInfoView(StatusWrapMixin, JsonResponseMixin, DetailView):
    """
    检查|新建|更新用户
    """
    model = TTUser
    http_method_names = ['get', 'post']
    include_attr = ['token', 'user_id', 'nick', 'money']

    def generate_session(self, count=64):
        ran = string.join(
            random.sample('ZYXWVUTSRQPONMLKJIHGFEDCBA1234567890zyxwvutsrqponmlkjihgfedcbazyxwvutsrqponmlkjihgfedcba',
                          count)).replace(" ", "")
        return ran

    def get_user(self, user_id):
        if not user_id:
            self.message = '信息缺失'
            self.status_code = SW.ERROR_DATA
            return False
        users = TTUser.objects.filter(user_id=user_id)
        if users.exists():
            user = users[0]
            return user
        self.message = '用户不存在'
        self.status_code = SW.INFO_NO_EXIST
        return False

    def get_object(self, queryset=None):
        user_id = self.request.GET.get('user_id', None)
        user = self.get_user(user_id)
        if user:
            return user
        self.message = '用户不存在'
        self.status_code = SW.INFO_NO_EXIST
        return user

    def post(self, request, *args, **kwargs):
        nick = request.POST.get('nick')
        avatar = request.POST.get('avatar')
        male = int(request.POST.get('male', 1))
        age = request.POST.get('age')
        sports = request.POST.get('sports')
        foods = request.POST.get('foods')
        province = request.POST.get('province')
        city = request.POST.get('city')
        country = request.POST.get('country')
        travel = request.POST.get('travel')
        user_id = request.POST.get('user_id')
        user = self.get_user(user_id)
        if not user:
            token = self.generate_session()
            user = TTUser(user_id=user_id)
            user.token = token
            user.money = 0.0
            user.pick = 0.0
            self.message = 'success'
            self.status_code = SW.INFO_SUCCESS
        user.nick = nick
        user.avatar = avatar
        user.male = male
        user.age = age
        user.sports = sports
        user.foods = foods
        user.travel = travel
        user.city = city
        user.country = country
        user.province = province
        user.save()
        return self.render_to_response({'user': user})


class GiftListView(CheckTokenMixin, StatusWrapMixin, MultipleJsonResponseMixin, ListView):
    """
    拥有的礼物列表
    """
    model = Gift
    paginate_by = 20

    def get_queryset(self):
        return super(GiftListView, self).get_queryset().filter(belong=self.user).order_by('-create_time')


class PetServiceView(CheckTokenMixin, StatusWrapMixin, JsonResponseMixin, DetailView):
    """
    洗澡、喂食
    """
    model = Pet
    http_method_names = ['get']
    include_attr = ['user_id', 'id', 'money', 'eated', 'showerd', 'belong']

    def get_object(self, queryset=None):
        objs = Pet.objects.filter(belong=self.user)
        if not objs.exists():
            self.message = '宠物不存在'
            self.status_code = SW.INFO_NO_EXIST
            return False
        obj = objs[0]
        aciton = int(self.request.GET.get('action', 1))
        if aciton == 1:
            if obj.eated:
                self.message = '不需要喂食'
                self.status_code = SW.INFO_EXISTED
                return False
            res = deduction(self.user, FOOD_PRICE)
            if not res:
                self.message = '余额不足'
                self.status_code = SW.ERROR_DATA
                return False
            obj.eated = True
            self.user.save()
            obj.save()
            return obj
        else:
            if obj.showerd:
                self.message = '不需要洗澡'
                self.status_code = SW.INFO_EXISTED
                return False
            res = deduction(self.user, SHOWER_PRICE)
            if not res:
                self.message = '余额不足'
                self.status_code = SW.ERROR_DATA
                return False
            obj.showerd = True
            self.user.save()
            obj.save()
            return obj


class ShitView(CheckTokenMixin, StatusWrapMixin, JsonResponseMixin, DetailView):
    """
    捡屎接口
    """
    include_attr = ['pick', 'money', 'user_id', 'id']

    def get_object(self, queryset=None):
        return None

    def get(self, request, *args, **kwargs):
        super(ShitView, self).get(request, *args, **kwargs)
        if not self.user.pick:
            self.message = '无屎可捡'
            self.status_code = SW.INFO_NO_EXIST
            return self.render_to_response({})
        self.user.money += 1
        self.user.pick -= 1
        self.user.save()
        return self.render_to_response({'user': self.user})


class EncounterListView(CheckTokenMixin, StatusWrapMixin, MultipleJsonResponseMixin, ListView):
    """
    邂逅列表
    """
    model = PetShip
    paginate_by = 20
    foreign = True
    exclude_attr = ['token', 'goods', 'sender', 'sender_gift', 'eated', 'showerd']

    def get_queryset(self):
        queryset = super(EncounterListView, self).get_queryset().filter(sender=self.user.user_pet.all()).order_by(
            'read',
            '-create_time')
        return queryset


class EncounterView(CheckTokenMixin, StatusWrapMixin, JsonResponseMixin, DetailView):
    """
    邂逅
    """

    model = PetShip
    pk_url_kwarg = 'mid'
    exclude_attr = ['token', 'goods', 'sender', 'sender_gift', 'eated', 'showerd']
    foreign = True

    def get_object(self, queryset=None):
        obj = super(EncounterView, self).get_object()
        obj.read = True
        obj.save()
        return obj
