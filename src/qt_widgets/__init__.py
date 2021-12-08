# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/8 5:53
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import config
import imp
from . import background

if config.DEBUG:
    imp.reload(background)
from .background import Background
