#! /env python
# -*- coding: utf-8 -*-

import re

def read_text(filename):
    with open(filename, mode='rt', encoding='utf-8') as file:
        text = file.read()
        sents = text.strip().split('\n')
        return [i.split('\t') for i in sents]


def replace_text(text_in, replace_rules):
    text_out = text_in
    for i in range(len(replace_rules)):
        pattern = replace_rules[i, 0]
        repl = replace_rules[i, 1]
        text_out = re.sub(pattern, repl, text_out, flags=re.DOTALL)
    return text_out