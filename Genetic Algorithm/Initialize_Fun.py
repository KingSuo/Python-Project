# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: Initialize_Fun.py                                                                
# @Time: 2017/10/23                                  
# @Contact: 648230502@qq.com
# @blog: 
# @Description:初始化种群函数 
"""
import numpy as np

def initialize_fun(population_size, chromosome_length):
    """
    
    :param population_size: 种群大小
    :param chromosome_length: 染色体长度
    :return:初始化染色体十进制数值列表（list）；shape = （population_size,） 
    """

    return list(np.random.randint(0, 2 ** chromosome_length - 1, population_size))