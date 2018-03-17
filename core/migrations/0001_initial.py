# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gift',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('use', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=100)),
                ('type', models.IntegerField(default=1, choices=[(1, '\u6c99\u76ae'), (2, '\u8428\u6469\u8036'), (3, '\u91d1\u6bdb'), (4, '\u8482\u59c6')])),
                ('sex', models.IntegerField(default=1, choices=[(0, '\u5973'), (1, '\u7537')])),
                ('character', models.CharField(default='', max_length=10)),
                ('wish', models.CharField(default='', max_length=10)),
                ('picture', models.CharField(max_length=120)),
                ('showerd', models.BooleanField(default=False)),
                ('eated', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PetShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('receiver', models.ForeignKey(related_name='ps_receiver', blank=True, to='core.Pet', null=True)),
                ('receiver_gift', models.ForeignKey(related_name='ps_receiver_gift', blank=True, to='core.Gift', null=True)),
                ('sender', models.ForeignKey(related_name='ps_sender', blank=True, to='core.Pet', null=True)),
                ('sender_gift', models.ForeignKey(related_name='ps_sender_gift', blank=True, to='core.Gift', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TTUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('modify_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('open_id', models.CharField(max_length=128)),
                ('session', models.CharField(max_length=128)),
                ('nick', models.CharField(default='', max_length=50)),
                ('male', models.IntegerField(default=1, choices=[(0, '\u5973'), (1, '\u7537')])),
                ('avatar', models.CharField(default='', max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='pet',
            name='belong',
            field=models.ForeignKey(related_name='user_pet', to='core.TTUser'),
        ),
        migrations.AddField(
            model_name='pet',
            name='encounter',
            field=models.ManyToManyField(related_name='pet_list', through='core.PetShip', to='core.Pet'),
        ),
        migrations.AddField(
            model_name='gift',
            name='belong',
            field=models.ForeignKey(related_name='user_presents', to='core.TTUser'),
        ),
        migrations.AddField(
            model_name='gift',
            name='goods',
            field=models.ForeignKey(related_name='good_gifts', to='core.Goods'),
        ),
    ]
