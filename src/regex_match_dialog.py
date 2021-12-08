# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/5 1:39
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

import setting
import regex_match


class RegexMatchDialog(QDialog):
    def __init__(self, parent=None):
        self.names = None
        super(RegexMatchDialog, self).__init__(parent)
        self.setWindowTitle("regex match")
        self.main_layout = QHBoxLayout(self)

        self.exp_line_edit = QLineEdit()
        self.match_bn = QPushButton("匹配")
        self.match_bn.clicked.connect(self.match)

        self.main_layout.addWidget(QLabel("正则表达式: "))
        self.main_layout.addWidget(self.exp_line_edit)
        self.main_layout.addWidget(self.match_bn)
        # 应用设置
        self.setting()

    def setting(self):
        fs = setting.get("font", None)
        if fs is None:
            fs = QFont().toString()
        f = QFont()
        f.fromString(fs)
        self.setFont(f)

    def match(self):
        self.names = list(regex_match.match(self.exp_line_edit.text()))
        self.close()


def exec_(parent=None):
    dia = RegexMatchDialog(parent)
    dia.exec_()
    return dia.names
