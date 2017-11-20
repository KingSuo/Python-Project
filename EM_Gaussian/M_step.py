# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: M_step.py                                                                
# @Time: 2017/10/20                                   
# @Contact: 648230502@qq.com
# @Description:M步：计算给定参数（可能性期望）后的均值 
"""

import numpy as np

def m_step(sample_list, possibility_list, means_list):
    """
    
    :param sample_list: 
    :param possibility_list: 
    :param means_list: 
    :return: 
    """
    sample_list_temp = list(sample_list)
    possibility_list_temp = list(possibility_list)
    means_list_temp = list(means_list)

    for i in range(len(means_list_temp)):
        numerator = [0 for _ in range(len(means_list_temp))]
        denominator = [0 for _ in range(len(means_list_temp))]
        for j in range(len(sample_list_temp)):
            numerator[i] += possibility_list_temp[j][i] * np.array(sample_list_temp[j])
            denominator[i] += possibility_list_temp[j][i]
        means_list_temp[i] = numerator[i] / denominator[i]
        del numerator
        del denominator

    return means_list_temp