# coding: utf-8
from __future__ import unicode_literals

from django.views.generic import ListView

from core.Mixin.CheckMixin import CheckSecurityMixin
from core.Mixin.StatusWrapMixin import StatusWrapMixin
from core.dss.Mixin import MultipleJsonResponseMixin
from core.models import Goods


class GoodsListView(StatusWrapMixin, MultipleJsonResponseMixin, ListView):
    model = Goods
    include_attr = ['id', 'name', 'price']
