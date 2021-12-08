# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/6 6:59
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import config
from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

import maya.cmds as mc

import setting
from qt_widgets import Background


class FontSettingWidget(Background):
    def __init__(self, parent=None):
        super(FontSettingWidget, self).__init__(parent)
        self.main_layout = QHBoxLayout(self)

        self.font = QLabel(self.font_setting())
        self.font_setting_bn = QPushButton("设置")
        self.font_setting_bn.clicked.connect(self.set_font_setting)
        self.main_layout.addWidget(QLabel("字体： "))
        self.main_layout.addWidget(self.font)
        self.main_layout.addWidget(self.font_setting_bn)

    def font_setting(self):
        f = setting.get("font", None)
        if f is None:
            return QFont().toString()
        return f

    def set_font_setting(self):
        a, b = QFontDialog.getFont()
        if type(a) == bool:
            ok = a
            f = b
        else:
            ok = b
            f = a
        if ok:
            setting.set("font", f.toString())
        else:
            mc.warning("取消了操作")


class RenameWidget(QWidget):
    def __init__(self, parent=None):
        super(RenameWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

        self.font_setting_widget = FontSettingWidget()
        self.main_layout.addWidget(self.font_setting_widget)
        self.main_layout.addStretch(0)


def new():
    return RenameWidget()
