# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/6 4:35
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

import rename
from utils import undo_block
from qt_widgets import Background


class AddNamePrefix(Background):
    def __init__(self, parent=None):
        super(AddNamePrefix, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)
        #
        self.body_layout = QHBoxLayout()

        self.prefix = QLineEdit()
        self.do_bn = QPushButton("添加")
        self.do_bn.clicked.connect(self.add_name_prefix)

        self.body_layout.addWidget(QLabel("前缀"))
        self.body_layout.addWidget(self.prefix)
        self.body_layout.addWidget(self.do_bn)
        #
        self.main_layout.addWidget(QLabel("添加名称前缀： "))
        self.main_layout.addLayout(self.body_layout)

    @undo_block
    def add_name_prefix(self):
        rename.add_name_prefix(self.prefix.text())


class ReplaceNameWidget(Background):
    def __init__(self, parent=None):
        super(ReplaceNameWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

        self.search_layout = QHBoxLayout()
        self.search = QLineEdit()
        self.search_layout.addWidget(QLabel("搜索："))
        self.search_layout.addWidget(self.search)

        self.replace_layout = QHBoxLayout()
        self.replace = QLineEdit()
        self.replace_layout.addWidget(QLabel("替换："))
        self.replace_layout.addWidget(self.replace)
        #
        self.do_bn_layout = QHBoxLayout()

        self.search_replace_bn = QPushButton("搜索替换")
        self.search_replace_bn.clicked.connect(self.search_replace)

        self.regex_search_replace_bn = QPushButton("正则搜索替换")
        self.regex_search_replace_bn.clicked.connect(self.regex_search_replace)

        self.do_bn_layout.addWidget(self.search_replace_bn)
        self.do_bn_layout.addWidget(self.regex_search_replace_bn)
        #
        self.main_layout.addWidget(QLabel("搜索替换名称： "))
        self.main_layout.addLayout(self.search_layout)
        self.main_layout.addLayout(self.replace_layout)
        self.main_layout.addLayout(self.do_bn_layout)
        self.main_layout.addStretch(0)

    @undo_block
    def search_replace(self):
        rename.search_replace_name(self.search.text(), self.replace.text())

    @undo_block
    def regex_search_replace(self):
        rename.regex_search_replace_name(self.search.text(), self.replace.text())


class RenameWidget(QWidget):
    def __init__(self, parent=None):
        super(RenameWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

        self.add_name_prefix = AddNamePrefix()
        self.replace_name = ReplaceNameWidget()

        self.main_layout.addWidget(self.add_name_prefix)
        self.main_layout.addWidget(self.replace_name)


def new():
    return RenameWidget()
