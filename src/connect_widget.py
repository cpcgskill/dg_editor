# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/20 6:06
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import config
import sys
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

import maya.cmds as mc

import attr_regex_match_dialog

from utils import undo_block


class FuncSelectWidget(QWidget):
    Connect, DisConnect = range(2)
    ConnectText = "建立连接"
    DisConnectText = "断开连接"

    def __init__(self, parent=None):
        super(FuncSelectWidget, self).__init__(parent)
        self.main_layout = QHBoxLayout(self)

        self.f_com = QComboBox(self)
        self.f_com.addItem(self.ConnectText)
        self.f_com.addItem(self.DisConnectText)

        self.main_layout.addWidget(QLabel("功能"))
        self.main_layout.addWidget(self.f_com)
        self.main_layout.addStretch(0)

    def func(self):
        if self.f_com.currentText() == self.ConnectText:
            return self.Connect
        else:
            return self.DisConnect


class MatchWidget(QWidget):
    def __init__(self, parent=None):
        super(MatchWidget, self).__init__(parent)
        self.main_layout = QHBoxLayout(self)
        self.name_text = QTextEdit()
        self.r_layout = QVBoxLayout()
        self.regex_match_bn = QPushButton("通过正则表达式匹配")
        self.regex_match_bn.clicked.connect(self.regex_match)
        self.r_layout.addWidget(self.regex_match_bn)
        self.r_layout.addStretch(0)

        self.main_layout.addWidget(self.name_text)
        self.main_layout.addLayout(self.r_layout)

    def regex_match(self):
        names = attr_regex_match_dialog.exec_(self)
        if names is None:
            mc.warning("取消了操作")
            return
        self.name_text.setPlainText("\n".join(names))

    def names(self):
        return list(self.name_text.toPlainText().splitlines())


class ConnectWidget(QWidget):
    def __init__(self, parent=None):
        super(ConnectWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

        self.func_sel_widget = FuncSelectWidget(self)
        self.match_out_attrs_widget = MatchWidget(self)
        self.match_in_attrs_widget = MatchWidget(self)
        self.do_bn = QPushButton("执行功能")
        self.do_bn.clicked.connect(self.do)

        self.main_layout.addWidget(self.func_sel_widget)
        self.main_layout.addWidget(QLabel("输出属性： "))
        self.main_layout.addWidget(self.match_out_attrs_widget)
        self.main_layout.addWidget(QLabel("输入属性： "))
        self.main_layout.addWidget(self.match_in_attrs_widget)
        self.main_layout.addWidget(self.do_bn)

    @undo_block
    def do(self):
        out_attrs = self.match_out_attrs_widget.names()
        in_attrs = self.match_in_attrs_widget.names()
        if len(out_attrs) != len(in_attrs):
            raise ValueError("输出输入属性数量不一致")
        if self.func_sel_widget.func() == FuncSelectWidget.Connect:
            for o, i in zip(out_attrs, in_attrs):
                mc.connectAttr(o, i)
        else:
            for o, i in zip(out_attrs, in_attrs):
                mc.disconnectAttr(o, i)


def new():
    return ConnectWidget()
