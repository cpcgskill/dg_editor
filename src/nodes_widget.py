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
from PySide2.QtGui import *
from PySide2.QtCore import Qt
from PySide2.QtWidgets import *

import maya.cmds as mc

import create_node_exp
import gen_name_exp_dialog
import regex_match_dialog

from utils import undo_block
from qt_widgets import Background

class CreateWidget(Background):
    def __init__(self, parent=None):
        super(CreateWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

        self.body_layout = QHBoxLayout()

        self.name_text = QTextEdit()
        self.create_exp_bn_layout = QVBoxLayout()
        self.create_exp_bn = QPushButton("通过表达式创建")
        self.create_exp_bn.setFixedWidth(120)
        self.create_exp_bn.clicked.connect(self.create_exp)
        self.create_exp_bn_layout.addWidget(self.create_exp_bn)
        self.create_exp_bn_layout.addStretch(0)

        self.body_layout.addWidget(self.name_text)
        self.body_layout.addLayout(self.create_exp_bn_layout)

        self.create_bn = QPushButton("创建")
        self.create_bn.clicked.connect(self.create_node)

        self.main_layout.addWidget(QLabel("创建： "))
        self.main_layout.addLayout(self.body_layout)
        self.main_layout.addWidget(self.create_bn)

    def create_exp(self):
        names = gen_name_exp_dialog.exec_(self)
        if names is None:
            mc.warning("取消了操作")
            return
        self.name_text.setText("\n".join(("{}: {}".format(n, t) for n, t in names)))

    @undo_block
    def create_node(self):
        exp = self.name_text.toPlainText()
        for n, t in create_node_exp.compile(exp):
            mc.createNode(t, n=n)


class DeleteWidget(Background):
    def __init__(self, parent=None):
        super(DeleteWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)

        self.body_layout = QHBoxLayout()

        self.name_text = QTextEdit()
        self.match_exp_bn_layout = QVBoxLayout()
        self.match_exp_bn = QPushButton("通过正则表达式匹配")
        self.match_exp_bn.setFixedWidth(120)
        self.match_exp_bn.clicked.connect(self.regex_match)
        self.match_exp_bn_layout.addWidget(self.match_exp_bn)
        self.match_exp_bn_layout.addStretch(0)

        self.body_layout.addWidget(self.name_text)
        self.body_layout.addLayout(self.match_exp_bn_layout)

        self.delete_bn = QPushButton("删除")
        self.delete_bn.clicked.connect(self.delete_nodes)

        self.main_layout.addWidget(QLabel("删除： "))
        self.main_layout.addLayout(self.body_layout)
        self.main_layout.addWidget(self.delete_bn)

    def regex_match(self):
        names = regex_match_dialog.exec_(self)
        if names is None:
            mc.warning("取消了操作")
            return
        self.name_text.setPlainText("\n".join(names))

    @undo_block
    def delete_nodes(self):
        nodes = list(self.name_text.toPlainText().splitlines())
        if len(nodes) < 1:
            return
        mc.delete(nodes)


class NodesWidget(QWidget):
    def __init__(self, parent=None):
        super(NodesWidget, self).__init__(parent)
        self.main_layout = QVBoxLayout(self)
        self.create_widget = CreateWidget(self)
        self.delete_widget = DeleteWidget(self)

        self.main_layout.addWidget(self.create_widget)
        self.main_layout.addWidget(self.delete_widget)


def new():
    return NodesWidget()
