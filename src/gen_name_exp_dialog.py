# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/22 5:35
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
import gen_name_exp


class GenNameDialog(QDialog):
    def __init__(self, parent=None):
        self.names = None
        super(GenNameDialog, self).__init__(parent)
        self.setWindowTitle("gen name")
        self.main_layout = QHBoxLayout(self)

        self.node_size = QSpinBox()
        self.node_size.setRange(5, 9999)
        self.exp_line_edit = QLineEdit()
        self.type_line_edit = QLineEdit()
        self.gen_bn = QPushButton("生成")
        self.gen_bn.clicked.connect(self.gen)

        self.main_layout.addWidget(QLabel("节点计数: "))
        self.main_layout.addWidget(self.node_size)
        self.main_layout.addWidget(QLabel("表达式: "))
        self.main_layout.addWidget(self.exp_line_edit)
        self.main_layout.addWidget(QLabel("节点类型: "))
        self.main_layout.addWidget(self.type_line_edit)
        self.main_layout.addWidget(self.gen_bn)
        # 应用设置
        self.setting()

    def setting(self):
        fs = setting.get("font", None)
        if fs is None:
            fs = QFont().toString()
        f = QFont()
        f.fromString(fs)
        self.setFont(f)

    def gen(self):
        node_size = self.node_size.value()
        exp = self.exp_line_edit.text()
        type_ = self.type_line_edit.text()
        values = [{"name_id": i} for i in range(node_size)]
        self.names = [(n, type_) for n in gen_name_exp.compile(exp, values)]
        self.close()


def exec_(parent=None):
    dia = GenNameDialog(parent)
    dia.exec_()
    return dia.names
