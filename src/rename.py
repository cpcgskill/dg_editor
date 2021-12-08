# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/6 5:37
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


def _selection_list_uids():
    sel = mc.ls(sl=True, l=True)
    nodes = [n for i in sel for o in ([i], mc.listRelatives(i, ad=True, pa=True)) for n in o]
    uids = mc.ls(nodes, uid=True)
    return uids


def add_name_prefix(prefix):
    for uid in _selection_list_uids():
        n = mc.ls(uid)[0]
        mc.rename(n, prefix + n.split("|")[-1])


def search_replace_name(search, replace):
    for uid in _selection_list_uids():
        n = mc.ls(uid)[0]
        sn = n.split("|")[-1]
        mc.rename(n, sn.replace(search, replace))


def regex_search_replace_name(search, replace):
    re_o = re.compile(search)
    for uid in _selection_list_uids():
        n = mc.ls(uid)[0]
        sn = n.split("|")[-1]
        mc.rename(n, re_o.sub(replace, sn))
