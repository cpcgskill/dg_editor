# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/22 6:14
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function

import re


class GenNameExpExc(Exception):
    pass


class TokenBase(object):
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return "{}<{}>".format(self.__class__.__name__, self.s)


class NameToken(TokenBase):
    pass


class ValueNameToken(TokenBase):
    pass


skip_space_match = re.compile(r"[ \t]+")
name_match = re.compile(r"[a-zA-Z0-9_]+")
value_name_match = re.compile(r"\{[a-zA-Z0-9_]+\}")


def _lex(exp):
    """

    :param exp: box_{value_name}
    :return:
    """
    while True:
        m = skip_space_match.match(exp)
        if not m is None:
            exp = exp[m.end():]
        if len(exp) == 0:
            return
        m = name_match.match(exp)
        if not m is None:
            token = NameToken(exp[m.start(): m.end()])
            exp = exp[m.end():]
            yield token
            continue
        m = value_name_match.match(exp)
        if not m is None:
            token = ValueNameToken(exp[m.start() + 1: m.end() - 1])
            exp = exp[m.end():]
            yield token
            continue
        raise GenNameExpExc("lex error")


def compile(exp, values):
    """

    :param exp: box_{value_name} or {value_name}_box or box_{value_name}_joint
    :param values: [{k: v, ...}, ...]
    :return:
    """
    tokens = list(_lex(exp))
    for kv in values:
        name = ""
        for t in tokens:
            if isinstance(t, NameToken):
                name += t.s
            else:
                v = kv.get(t.s)
                if v is None:
                    raise GenNameExpExc("ket not fount")
                name += str(v)
        yield name


if __name__ == "__main__":
    test_exp = "box_{name_id}_joint"
    print("test lex")
    print(list(_lex(test_exp)))
    print("test compile")
    print(list(compile(test_exp, [
        {"name_id": 0},
        {"name_id": 1},
        {"name_id": 2},
        {"name_id": 3},
    ])))
