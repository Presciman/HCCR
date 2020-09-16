# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 12:01:54 2018

@author: MJK
"""

import pprint, pickle

pkl_file = open('result.dict', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)
#
#data2 = pickle.load(pkl_file)
#pprint.pprint(data2)

pkl_file.close()