# coding: utf-8
from __future__ import unicode_literals
from django.db import models


# Create your models here.


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TTUser(BaseModel):
    sex_choices = [(0, '女'),
                   (1, '男')]

    name = models.CharField(max_length=100)
    open_id = models.CharField(max_length=128)
    session = models.CharField(max_length=128)
    nick = models.CharField(max_length=50, default='')
    male = models.IntegerField(default=1, choices=sex_choices)
    avatar = models.CharField(max_length=128, default='')

    def __unicode__(self):
        return self.name


class Goods(BaseModel):
    name = models.CharField(max_length=50)
    price = models.FloatField(default=1)
    picture = models.CharField(max_length=128, default='', null=True, blank=True)

    def __unicode__(self):
        return '{0}-{1}'.format(self.name, self.price)


class Gift(BaseModel):
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=128, default='', null=True, blank=True)
    use = models.BooleanField(default=False)

    belong = models.ForeignKey(TTUser, related_name='user_presents')
    goods = models.ForeignKey(Goods, related_name='good_gifts')

    def __unicode__(self):
        return self.name


class Pet(BaseModel):
    type_choices = [(1, '沙皮'),
                    (2, '萨摩耶'),
                    (3, '金毛'),
                    (4, '蒂姆')]

    sex_choices = [(0, '女'),
                   (1, '男')]

    name = models.CharField(max_length=100, default='')
    type = models.IntegerField(default=1, choices=type_choices)
    sex = models.IntegerField(default=1, choices=sex_choices)
    character = models.CharField(max_length=10, default='')
    wish = models.CharField(max_length=10, default='')
    picture = models.CharField(max_length=120)

    showerd = models.BooleanField(default=False)
    eated = models.BooleanField(default=False)

    belong = models.ForeignKey(TTUser, related_name='user_pet')
    encounter = models.ManyToManyField("self", related_name='pet_list', through='PetShip', symmetrical=False,
                                       through_fields=('sender', 'receiver'))

    def __unicode__(self):
        return '{0}-{1}'.format(self.belong.name, self.name)


class PetShip(BaseModel):
    sender = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True, related_name='ps_sender')
    receiver = models.ForeignKey(Pet, on_delete=models.CASCADE, null=True, blank=True, related_name='ps_receiver')
    sender_gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True,
                                    related_name='ps_sender_gift')
    receiver_gift = models.ForeignKey(Gift, on_delete=models.CASCADE, null=True, blank=True,
                                      related_name='ps_receiver_gift')

    def __unicode__(self):
        return '{0}->{1}'.format(self.sender.name, self.receiver.name)