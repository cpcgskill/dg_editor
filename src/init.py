# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/17 5:12
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
import imp
import config

imp.reload(config)

# 导入所有需要的模块
import qt_widgets

import create_node_exp
import regex_match
import attr_regex_match
import rename
import setting

import gen_name_exp_dialog
import regex_match_dialog
import attr_regex_match_dialog

import nodes_widget
import connect_widget
import rename_widget
import setting_widget

import main_window

# 模块列表
modules = [
    qt_widgets,

    create_node_exp,
    regex_match,
    attr_regex_match,
    rename,
    setting,

    gen_name_exp_dialog,
    regex_match_dialog,
    attr_regex_match_dialog,

    nodes_widget,
    connect_widget,
    rename_widget,
    setting_widget,

    main_window,
]
if config.DEBUG:
    # 在DEBUG下reload所有模块
    for m in modules:
        imp.reload(m)
