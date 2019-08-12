#!/usr/bin/env python
# -*- coding: utf-8 -*-
# By Yuhwa Choong


import string

l_chars = string.ascii_lowercase
u_chars = string.ascii_uppercase

value_list = list(range(1, 27))
c_dict = dict(dict(zip(l_chars, value_list)), **dict(zip(u_chars, value_list)))


def cal_value(word):
    tot = 0
    o_str = ''
    for char in word:
        this_v = c_dict.get(char, 0)
        tot += this_v
        o_str += str(this_v) + '+'
    o_str = o_str[0:-1]
    return tot, o_str


if __name__ == '__main__':
    while True:
        a = input()
        tot, o_str = cal_value(a)
        print(tot)
        print(o_str)
