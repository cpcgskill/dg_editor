# -*-coding:utf-8 -*-
u"""
:创建时间: 2021/11/21 6:38
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:QQ: 2921251087
:爱发电: https://afdian.net/@Phantom_of_the_Cang
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127

"""
from __future__ import unicode_literals, print_function
import re


class TokenBase(object):
    def __init__(self, s):
        self.s = s


class NameToken(TokenBase):
    pass


class CoToken(TokenBase):
    pass


class LFToken(TokenBase):
    pass


class ExpExc(Exception):
    pass


name_match = re.compile(r"[a-zA-Z0-9_]+")
co_match = re.compile(r":")
lf_match = re.compile(r"\n|\r\n")
skip_space_match = re.compile(r"[ \t]+")


def _lex(exp):
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
        m = co_match.match(exp)
        if not m is None:
            token = CoToken(":")
            exp = exp[1:]
            yield token
            continue
        m = lf_match.match(exp)
        if not m is None:
            token = LFToken(exp[m.start(): m.end()])
            exp = exp[m.end():]
            yield token
            continue
        raise ExpExc("lex error")


def compile(exp):
    tokens = list(_lex(exp))
    while True:
        if len(tokens) == 0:
            return
        t = tokens[0]
        if isinstance(t, LFToken):
            tokens.pop(0)
            continue
        if isinstance(tokens[0], NameToken) and \
                isinstance(tokens[1], CoToken) and \
                isinstance(tokens[2], NameToken):
            yield tokens[0].s, tokens[2].s
            tokens = tokens[3:]
            continue
        raise ExpExc("syntax error")


if __name__ == "__main__":
    test_exp = """\t
\r\n
locator1: transform
locator1: transform
    """
    print("test lex")
    print(list(compile(test_exp)._lex()))

    print("test synex")
    print(list(compile(test_exp)))
