# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/5 7:38
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

import re

import maya.cmds as mc


def match(exp):
    re_o = re.compile(exp)
    for n in mc.ls("*"):
        for attr in mc.listAttr(n):
            attr = "{}.{}".format(n, attr)
            m = re_o.match(attr)
            if not m is None:
                if m.group() == attr:
                    yield attr
