# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 19:20:16 2022

@author: ARYAMAN
"""
word_list =[]

with open("corncob_caps.txt", "r") as words:
	   lines = words.readlines()

final_list = []

for l in lines:
    final_list.append(l.replace("\n","")) 