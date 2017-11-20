# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: Mutate_Fun.py                                                                
# @Time: 2017/10/23                            
# @Contact: 648230502@qq.com
# @blog: 
# @Description:变异函数 
"""
import numpy as np

def mutate_fun(son_chromosomes_list, key=None, isReturnDecimalism=1):
    """
    
    :param son_chromosomes_list:子代染色体列表（list），两个元素 
    :param key: 用于修改变异基因个数
    :param isReturnDecimalism: 是否返回十进制数值
    :return: 变异后的染色体
    """
    if isinstance(son_chromosomes_list[0], str):    #是符串表示的二进制，则直接调用
        son1_chromosome = son_chromosomes_list[0]
        son2_chromosome = son_chromosomes_list[1]
    else:                                           #是十进制数值表示的，需转化为二进制字符串来处理
        son1_chromosome = bin(son_chromosomes_list[0]).split('0b')[1]
        son2_chromosome = bin(son_chromosomes_list[1]).split('0b')[1]

    print('son1_chromosome: ', son1_chromosome)
    print('son2_chromosome: ', son2_chromosome)
    #产生两个随机变异点
    mutate_point1_lower = np.random.randint(0, len(son1_chromosome))      #变异点下限
    mutate_point1_upper = mutate_point1_lower + 1 if key is None else key(mutate_point1_lower)      #变异点上限
    mutate_point2_lower = np.random.randint(0, len(son2_chromosome))
    mutate_point2_upper = mutate_point2_lower + 1 if key is None else key(mutate_point2_lower)

    point1_str = '1' * (mutate_point1_upper - mutate_point1_lower) + '0' * (len(son1_chromosome) - mutate_point1_upper)
    point2_str = '1' * (mutate_point1_upper - mutate_point1_lower) + '0' * (len(son2_chromosome) - mutate_point2_upper)
    print('point1_lower: ', mutate_point1_lower)
    print('point2_lower: ', mutate_point2_lower)
    print('point1_str: ', point1_str)
    print('point2_str: ', point2_str)

    #异或操作符^可以用‘1’将指定位置取反：相同为0不同为1
    son1_mutate_chromosome = int(son1_chromosome, 2) ^ int(point1_str, 2)
    son2_mutate_chromosome = int(son2_chromosome, 2) ^ int(point2_str, 2)
    print('son1_mutate_chromosome: ', son1_mutate_chromosome)
    print('son2_mutate_chromosome: ', son2_mutate_chromosome)

    if isReturnDecimalism:
        return [son1_mutate_chromosome, son2_mutate_chromosome]
    else:
        return [bin(son1_mutate_chromosome).split('0b')[1], bin(son2_mutate_chromosome).split('0b')[1]]

# mutate_fun([132053, 897452])
# son1_chromosome:  100000001111010101
# son2_chromosome:  11011011000110101100
# point1_lower:  5

# point2_lower:  14
# point1_str:  1000000000000
# point2_str:  1000
# son1_mutate_chromosome:  136149
# son2_mutate_chromosome:  897444
# son1_mutate_chromosome:  100001001111010101
# son2_mutate_chromosome:  11011011000110100100

# mutate_fun([132053, 897452], key=lambda p: p + 5)
# son1_chromosome:  100000001111010101
# son2_chromosome:  11011011000110101100
# point1_lower:  13
# point2_lower:  3
# point1_str:  11111
# point2_str:  11111000000000000
# son1_mutate_chromosome:  132042
# son2_mutate_chromosome:  803244
# son1_mutate_chromosome:  100000001111001010
# son2_mutate_chromosome:  11000100000110101100