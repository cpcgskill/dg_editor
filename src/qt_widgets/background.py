# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/8 5:53
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


class Background(QWidget):
    def paintEvent(self, *args, **kwargs):
        p = QPainter(self)
        p.setPen(Qt.NoPen)
        p.setBrush(QBrush(QColor(65, 65, 65)))
        p.drawRect(self.rect())
        p.end()
