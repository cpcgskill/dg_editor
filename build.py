# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/19 3:40
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

# 因为是将库放在C:\Users\PC\Documents\maya\scripts下的所以需要初始化maya
try:
    import maya.standalone

    maya.standalone.initialize()
except:
    pass

import CPCLI.core as cli_core
from CPCLI.overall_processing_function import group
from CPCLI.file_filtering_functions import noTypes
from CPCLI.processing_function import deleteBlankLines, deleteUselessStrings


class Config(object):
    # 文件过滤函数
    file_filtering_functions = [
        noTypes(['pyc'])
    ]
    # 整体处理函数
    overall_processing_function = [
        group(
            name=u"DG_EDITOR_0_1_0",
            exec_script=u'''\
import main
from main import main
main()'''
        )
    ]
    # 处理函数
    processing_function = [
        # 清除空行
        deleteBlankLines,
        # 清除无用字符串
        deleteUselessStrings
    ]
    # 可真可假影响不大
    debug = True

    class Path(object):
        root = r"D:\dev\python_for_maya\tool\dg_editor"
        src = root + r"\src"
        scripts = root + r"\script"
        build = root + r"\build"


cli_core.build(Config)