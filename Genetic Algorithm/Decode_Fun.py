# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: Decode_Fun.py                                                                
# @Time: 2017/10/23                            
# @Contact: 648230502@qq.com
# @blog: 
# @Description:解码函数 
"""

def decode_fun(chromosome, chromosome_length=17, lower_bound=0, upper_bound=9):
    """
    
    :param chromosome:二进制数值字符串类型或十进制数值类型。字符串类型如：'0101100110110'，或者使用'0b0101010101'，即以
    '0b'开头的二进制表示方法，两种方式需要指明清楚
    :param chromosome_length:二进制数值长度
    :param lower_bound: 实际取值的实数下限
    :param upper_bound:实际取值的实数上限 
    :return:二进制染色体对应的实数值 
    """
    if isinstance(chromosome, str):
        chromosome_temp = int(chromosome, 2)    #将表示二进制的字符串转换为十进制数值
    else:
        chromosome_temp = round(float(chromosome), 4)   #如果为十进制数，那么直接使用

    return lower_bound + chromosome_temp * ((upper_bound - lower_bound) / (2 ** chromosome_length - 1))