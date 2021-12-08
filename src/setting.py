# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/12/6 7:08
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import config
import os
import json
import codecs

SETTING_FILE = os.path.join(config.PATH, "setting.json")


def _open_setting_file():
    if not os.path.isfile(SETTING_FILE):
        with codecs.open(SETTING_FILE, "w", encoding="utf-8") as f:
            json.dump(dict(), f)
    with codecs.open(SETTING_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def _save_setting_file(data):
    with codecs.open(SETTING_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f)


def set(key, val):
    data = _open_setting_file()
    data[key] = val
    _save_setting_file(data)


def get(key, default):
    data = _open_setting_file()
    return data.get(key, default)
