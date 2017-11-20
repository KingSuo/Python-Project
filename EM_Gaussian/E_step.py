# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: E_step.py                                                                
# @Time: 2017/10/20                                   
# @Contact: 648230502@qq.com
# @Description:E步：计算给定参数值（均值）后可能性的期望 
"""

import numpy as np

def e_step(sample_list, possibility_list, means_list):
    """
    
    :param sample_list:样本列表 
    :param possibility_list: 可能性列表，即隐藏变量列表
    :param means_list: 均值列表
    :return:更新后的可能性列表 
    """
    sample_list_temp = list(sample_list)
    possibility_list_temp = list(possibility_list)
    means_list_temp = list(means_list)
    zeta = 1
    for i in range(len(sample_list_temp)):
        numerator = [1 for _ in range(len(means_list_temp))]    #定义分子列表（list）
        for j in range(len(means_list_temp)):
            temp = np.array(sample_list_temp[i] - means_list_temp[j])
            numerator[j] = np.exp(-1 * np.dot(temp, temp) / (2 * zeta ** 2))    #分子
            # print('sample_list_temp[i]: ', sample_list_temp[i])
            # print('means_list_temp[j]', means_list_temp[j])
            # print('temp: ', temp)
        denominator = sum(numerator)    #分母
        # print('numerator: ', numerator)
        # print('denominator: ', denominator)
        possibility_list_temp[i] = numerator / denominator      #求隐藏变量的期望
        # for m in range(len(means_list_temp)):
        #     possibility_list_temp[i][m] = round(numerator[m] / denominator, 6)
        del numerator

    return possibility_list_temp