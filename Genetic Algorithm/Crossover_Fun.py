# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: Crossover_Fun.py                                                                
# @Time: 2017/10/23                                   
# @Contact: 648230502@qq.com
# @blog: 
# @Description:交叉函数 
"""
import numpy as np

def crossover_fun(parent_chromosomes_list, chromosome_length=17, isReturnDecimalism=1):
    """
    
    :param parent_chromosomes_list:父代染色体列表，包括父染色体和母染色体（list） 
    :param isReturnDecimalism: 是否返回十进制数值（bool）
    :return: 子代染色体列表（list）
    """

    #将'0b0101..'形式的二进制表示方式转为'0101001..'字符串格式
    father_chromosome = bin(parent_chromosomes_list[0]).split('0b')[1]
    mother_chromosome = bin(parent_chromosomes_list[1]).split('0b')[1]
    f_add_zero_len = chromosome_length - len(father_chromosome)
    m_add_zero_len = chromosome_length - len(mother_chromosome)

    #通过向字符串左侧添加字符'0'来使两个字符串长度相等
    if f_add_zero_len > 0:
        father_chromosome = '0' * f_add_zero_len + father_chromosome
    if m_add_zero_len > 0:
        mother_chromosome = '0' * m_add_zero_len + mother_chromosome

    print('father_chromosome: ', father_chromosome)
    print('mother_chromosome: ', mother_chromosome)

    lower_bound_temp = 999999999     #定义交叉片段的起始标签下限
    upper_bound_temp = 0     #定义交叉片段的终止标签上限
    #如果下限值比上限值大，或者两者之差大于染色体长度的一半以上，则执行while循环
    while(lower_bound_temp > upper_bound_temp or (upper_bound_temp - lower_bound_temp) > 0.5 * len(father_chromosome)):

        lower_bound_temp = np.random.randint(0, len(father_chromosome))
        upper_bound_temp = np.random.randint(0, len(father_chromosome))
        if lower_bound_temp == upper_bound_temp:
            upper_bound_temp += 1
    lower_bound = lower_bound_temp
    upper_bound = upper_bound_temp
    crossover_slice = slice(lower_bound, upper_bound)      #定义交叉片段的切片（slice）
    save_slice1 = slice(0, lower_bound)     #定义保留切片1（slice）
    save_slice2 = slice(upper_bound, len(father_chromosome))     #定义保留切片2（slice）
    print('save_slice1: ', save_slice1)
    print('crossover_slice: ', crossover_slice)
    print('save_slice2: ', save_slice2)

    son1_cross_chromosome = father_chromosome[save_slice1] + mother_chromosome[crossover_slice] + father_chromosome[save_slice2]
    son2_cross_chromosome = mother_chromosome[save_slice1] + father_chromosome[crossover_slice] + mother_chromosome[save_slice2]

    print('son1_cross_chromosome: ', son1_cross_chromosome)
    print('son2_cross_chromosome: ', son2_cross_chromosome)

    if isReturnDecimalism:
        return [int(son1_cross_chromosome, 2), int(son2_cross_chromosome, 2)]     #返回十进制数值（int）
    else:
        return [son1_cross_chromosome, son2_cross_chromosome]     #返回二进制字符串（string）

# print(crossover_fun([132005, 897500]))