# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: Liner_Search_Algorithm.py                                                                
# @Time: 2017/10/30                             
# @Contact: 648230502@qq.com
# @Description:线性搜索算法 

阻尼法
线性搜索算法：theta = Arg_theta Min（f(x + theta * d)）；即求参数theta，使得函数f取最小值
"""
import numpy as np


def linear_search(x=[], d=[], key=None):
    """

    :param x:当前因素取值 
    :param d: 搜索方向
    :param key: 函数表达式;即key(x, d, theta)
    :return: theta，使得函数值取最小的参数
    """
    x_stic = np.array(x).astype(float)
    d_stic = np.array(d).astype(float)
    f_list_temp0 = []
    f_list_temp1 = []
    f_list_temp2 = []
    for i in range(20):
        f_list_temp0.append(key(x_stic, d_stic, i * 0.1))  # 从0-20中以步长为0.1取值
        f_list_temp1.append(key(x_stic, d_stic, i * 0.01))  # 从0-2中以步长为0.01取值
        f_list_temp2.append(key(x_stic, d_stic, i * 0.001))  # 从0-0.2中以步长为0.001取值

    if min(f_list_temp0) <= min(f_list_temp1):
        print('min value: ', min(f_list_temp0))
        # if min(f_list_temp0) != min(f_list_temp0):
        # print(f_list_temp0)
        index = 0
        for i in f_list_temp0:
            if i == min(f_list_temp0):
                theta = index * 0.1
                if theta == 0:
                    index_new = 0
                    for j in f_list_temp2:
                        if j == min(f_list_temp2):
                            theta = index_new * 0.001
                            break
                        index_new += 1
                break
            index += 1
    else:
        print('min value: ', min(f_list_temp1))
        # if min(f_list_temp1) != min(f_list_temp1):
        # print(f_list_temp1)
        index = 0
        for i in f_list_temp1:
            if i == min(f_list_temp1):
                theta = index * 0.01
                if theta == 0:
                    index_new = 0
                    for j in f_list_temp2:
                        if j == min(f_list_temp2):
                            theta = index_new * 0.001
                            break
                        index_new += 1
                break
            index += 1
    print('theta: ', theta)

    return theta