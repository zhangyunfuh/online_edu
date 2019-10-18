# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-22 21:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='咨询者姓名')),
                ('phone', models.CharField(max_length=11, verbose_name='咨询者手机')),
                ('course', models.CharField(max_length=20, verbose_name='咨询课程')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='咨询时间')),
            ],
            options={
                'verbose_name_plural': '用户咨询信息',
                'verbose_name': '用户咨询信息',
            },
        ),
        migrations.CreateModel(
            name='UserComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300, verbose_name='评论内容')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='评论时间')),
            ],
            options={
                'verbose_name_plural': '用户评论信息',
                'verbose_name': '用户评论信息',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户学习课程信息',
                'verbose_name': '用户学习课程信息',
            },
        ),
        migrations.CreateModel(
            name='UserLove',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('love_id', models.IntegerField(verbose_name='收藏id')),
                ('love_type', models.IntegerField(choices=[(1, '机构'), (2, '课程'), (3, '教师')], verbose_name='收藏类型')),
                ('love_status', models.BooleanField(default=False, verbose_name='收藏状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='收藏时间')),
            ],
            options={
                'verbose_name_plural': '收藏信息',
                'verbose_name': '收藏信息',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg_user', models.IntegerField(verbose_name='消息用户')),
                ('msg_content', models.CharField(max_length=100, verbose_name='消息内容')),
                ('msg_status', models.BooleanField(default=False, verbose_name='消息状态')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name_plural': '用户消息信息',
                'verbose_name': '用户消息信息',
            },
        ),
    ]
