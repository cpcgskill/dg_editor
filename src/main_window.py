# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/19 3:46
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
from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *
from maya.OpenMayaUI import MQtUtil
from shiboken2 import wrapInstance

import setting

import nodes_widget
import connect_widget
import rename_widget
import setting_widget


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        if sys.version_info.major >= 3:
            self.setParent(wrapInstance(int(MQtUtil.mainWindow()), QWidget))
        else:
            self.setParent(wrapInstance(long(MQtUtil.mainWindow()), QWidget))
        self.setWindowFlags(Qt.Window)

        self.setWindowTitle("dg editor {}".format(config.VERSION))

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.tab = QTabWidget(self)
        self.main_layout.addWidget(self.tab)
        self.tab.addTab(nodes_widget.new(), "节点")
        self.tab.addTab(connect_widget.new(), "连接")
        self.tab.addTab(rename_widget.new(), "名称")
        self.tab.addTab(setting_widget.new(), "设置")

        # 应用设置
        self.setting()

    def setting(self):
        fs= setting.get("font", None)
        if fs is None:
            fs = QFont().toString()
        f = QFont()
        f.fromString(fs)
        self.setFont(f)


def new():
    win = MainWindow()
    win.show()
    if config.DEBUG:
        return win
