# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: CalculatePrice.py                                                                
# @Time: 2017/11/18                               
# @Contact: 648230502@qq.com
# @blog: 
# @Description: 
"""

import numpy as np

def calculate_price(price_class, bgr_means_list, lower_attribute_array, upper_attribute_array):
    """
    
    :param price_class: 价格类（class）
    :param bgr_means_list: bgr均值（list）
    :param lower_attribute_array: 价格属性变化下限（array）
    :param upper_attribute_array: 价格属性变化上限（array）
    :return:显示信息，包括颜色尺寸及价格（list） 
    """
    lower_attribute_array_temp = np.array(lower_attribute_array)
    upper_attribute_array_temp = np.array(upper_attribute_array)
    show_info_list = []
    for i in range(len(bgr_means_list)):
        lower_bias = lower_attribute_array_temp - bgr_means_list[i]
        upper_bias = upper_attribute_array_temp - bgr_means_list[i]
        lower_bias_sum = lower_bias.sum(axis=1)
        upper_bias_sum = upper_bias.sum(axis=1)
        lower_bias_prod = lower_bias.prod(axis=1)
        upper_bias_prod = upper_bias.prod(axis=1)
        for j in range(len(lower_bias)):
            flag = 0
            if lower_bias_sum[j] < 0 and upper_bias_sum[j] > 0 and lower_bias_prod[j] > 0 and upper_bias_prod[j] > 0:
                for k in range(len(lower_bias[j])):
                    if lower_bias[j][k] <= 0 and upper_bias[j][k] >= 0:
                        flag += 1
            if flag == len(lower_bias[0]):
                break
        color_size_str = price_class.color_size_list[j]
        price = price_class.price_list[j]
        show_info_list.append([color_size_str, price])

    return show_info_list
