# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: EM_Algorithm.py                                                                
# @Time: 2017/10/20                                   
# @Contact: 648230502@qq.com
# @Description:EM算法——上帝算法
# 参考http://blog.csdn.net/zkl99999/article/details/50968836
2017.10.20

本算法是针对高斯分布的期望最大化实现算法。对两组或两组以上给定标准差相同的高斯数值分布，进行求参数均值
EM大法好啊~~~~~~

"""

from E_step import e_step
from M_step import m_step
import numpy as np

#zeta为分布的方差
zeta = 1

def em_algorithm(sample_list, number_of_kinds=2, threshold_value=0.001, max_iteration=20):
    """
    
    :param sample_list:list类型数据，每行为一个样本数据 
    :param number_of_kinds: int类型数据，指定类别数
    :param threshold_value: 终止阈值
    :param max_iteration: 最大迭代次数
    :return: list类型均值，list类型的样本判为每个类别的可能性大小
    """
    if isinstance(sample_list[0], (int, float)):    #如果传入的列表中的元素是数值类型，而不是列表类型，则将其改为列表类型
        sample_list_temp = [[i] for i in sample_list]
    else:
        sample_list_temp = sample_list
    means_list = list(np.random.random((number_of_kinds, len(sample_list_temp[0]))))  #初始化均值列表
    temp = [0 for i in range(number_of_kinds)]
    possibility_list = [temp for i in range(len(sample_list_temp))] #初始化可能性列表

    k = 0
    change_rate = 9999999999999
    while(change_rate > threshold_value):
        print('k: ', k)
        if k >= max_iteration:
            print('Times of iteration too many!')
            break
        possibility_list = e_step(sample_list=sample_list_temp, possibility_list=possibility_list, means_list=means_list)
        means_list_old = list(means_list)
        means_list = m_step(sample_list=sample_list_temp, possibility_list=possibility_list, means_list=means_list)
        means_list_new = list(means_list)
        temp0 = [0 for i in range(number_of_kinds)]

        for i in range(len(temp)):
            temp1 = means_list_new[i] - means_list_old[i]
            temp0[i] = np.dot(temp1, temp1)
            del temp1

        change_rate = sum(temp0)
        if change_rate < threshold_value:
            print('change not enough!')
        print('change_rate: ', change_rate)
        print('means_list: ', means_list)
        del temp0
        k += 1

    return means_list, possibility_list