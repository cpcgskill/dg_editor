# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/6 5:48
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import imp
import init

imp.reload(init)

import rename

import maya.mel as mel

mel.eval("""
polySphere -r 1 -sx 20 -sy 20 -ax 0 1 0 -cuv 2 -ch 1;
// 结果: pSphere1 polySphere1 // 
select -r pSphere1 ;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
doGroup 0 1 1;
duplicate -rr;
//结果: group7 //
select -add group6 ;
""")
rename.add_name_prefix("_")
rename.search_replace_name("gr", "gra")
rename.regex_search_replace_name("o.p", "urp")
