# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: test.py                                                                
# @Time: 2017/10/22                                   
# @Contact: 648230502@qq.com
# @Description:EM算法——上帝算法 
"""
from EM_Algorithm import em_algorithm
import numpy as np

a = np.random.normal(1.5, 1, 1000)
b = np.random.normal(3, 1, 1000)
c = np.random.normal(-2, 1, 1000)
sample_list = list(a) + list(b) + list(c)
print(sample_list)

means, possibility = em_algorithm(sample_list=sample_list, number_of_kinds=3, threshold_value=0.00001)
print('possibility: ', possibility)