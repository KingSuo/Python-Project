# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: Fitness_Fun.py                                                                
# @Time: 2017/10/23                                   
# @Contact: 648230502@qq.com
# @blog: 
# @Description: 适应度函数
"""
from Decode_Fun import decode_fun

def fitness_fun(population_list, chromosome_length=17, lower_bound=0, upper_bound=9, key=None):
    """
    
    :param population_list: 种群列表（list）,其元素为十进制数值
    :param key:适应度函数表达式 
    :return: 种群适应度值（dict）
    """
    population_list_temp = list(population_list)
    fitness_dict = {key(decode_fun(chromosome=i, chromosome_length=chromosome_length, lower_bound=lower_bound, \
                                   upper_bound=upper_bound)): i for i in population_list_temp}

    return fitness_dict
# fitness_fun([12, 45, 6, 8, 4, 5], key=lambda i: i * 0.5)