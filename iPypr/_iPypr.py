#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

class pypr(object):
    def __init__(self, ks, tag = "\t"):
        self.ks = ks
        self.tag = tag
        self.pr(ks)

    def _topr(self, k = 0, v = "", flag = 1):
        unitype = unicode if sys.version < '3' else str
        if type(v) in (int, float, str, bool, type(None), unitype):
            v = '"%s"' %v if type(v) in (str, unitype) else v
            print('%s[%s] => %s' %(self.tag*flag,k,v))
        else:
            print("%s[%s] => " %(self.tag*flag,k),end='')
            vflag = flag + 1
            self.pr(v, vflag)

    def pr(self, ks = None, flag = 1, pre = "", pro = ""):
        tps = {
            list : ("List(%s) [", "]"),
            dict : ("Dict(%s) {", "}"),
            tuple : ("Tuple(%s) (", ")"),
        }
        pre, pro = tps[type(ks)]
        print(pre % len(ks))
        for k in ks:
            k, v = (k, ks[k]) if type(ks) == dict else (ks.index(k), k)
            self._topr(k, v, flag)
        print(self.tag*(flag-1)+pro)

