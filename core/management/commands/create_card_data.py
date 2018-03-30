# coding: utf-8
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from core.models import TTUser, PetShip


class Command(BaseCommand):
    def handle(self, *args, **options):
        mes = TTUser.objects.filter(
            user_id__in=('50227463264', '53612212509', '80081895938', '68152714750', '52707073333'))
        # count = mes.count()
        # me = mes[random.randint(0, count - 1)]
        for me in mes:
            for re in mes:
                if not PetShip.objects.filter(sender=me.user_pet.all()[0], receiver=re.user_pet.all()[0]).exists():
                    PetShip(sender=me.user_pet.all()[0], receiver=re.user_pet.all()[0]).save()
                if not PetShip.objects.filter(sender=re.user_pet.all()[0], receiver=me.user_pet.all()[0]).exists():
                    PetShip(sender=re.user_pet.all()[0], receiver=me.user_pet.all()[0]).save()
