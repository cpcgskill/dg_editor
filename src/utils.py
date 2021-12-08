# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/8 4:54
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

import functools
import maya.cmds as mc


def undo_block(fn):
    @functools.wraps(fn)
    def _(*args, **kwargs):
        mc.undoInfo(ock=True)
        try:
            return fn(*args, **kwargs)
        finally:
            mc.undoInfo(cck=True)

    return _
