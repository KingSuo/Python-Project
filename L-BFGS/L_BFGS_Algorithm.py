# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: L_BFGS_Algorithm.py                                                                
# @Time: 2017/10/30                             
# @Contact: 648230502@qq.com
# @Description:L-BFGS算法 
#参考Wiki百科：https://en.wikipedia.org/wiki/Limited-memory_BFGS

L-BFGS:限制内存拟牛顿法（limited-memory BFGS）；
基本思想：不再存储完整的矩阵Dk，而是存储计算过程中的向量序列{s_i},{y_i},需要矩阵Dk时，利用向量序列{s_i}，{y_i}的计算来代
替。而且，向量序列{s_i}，{y_i}也不是所有的都存储，而是固定存最新的m个（参数m可以由用户根据自己的机器内存自行指定）。每次
计算Dk时，只用到最新的m个{s_i}和m个{y_i},、。显然，这样一来，将存储由原来的O（N**2）降到了O（mN）。
"""
from Linear_Search_Algorithm import linear_search
from Two_Loop_Recursion_Algorithm import two_loop
import numpy as np

def L_BFGS(x_0, threshold_value=0.0001, m=5, key1=None, key2=None):
    """
    
    :param x_0: 初始值
    :param threshold_value: 
    :param m: 
    :param key1: 函数f
    :param key2: 函数f的导数
    :return: 
    """
    x0 = np.array(x_0).astype(float)
    print('初始值x0 : ', x0)
    s_list = []     #元素为s_i= x_i+1 - x_i，i取0,1...k-1，k为第k次迭代
    y_list = []     #元素为y_i= g_i+1 - g_i，i取0,1...k-1，k为第k次迭代
    g_k1_dis = 9999999999   #定义偏导数平方和
    k = 0
    while(g_k1_dis > threshold_value):
        if k >= 100:
            print('Iteration times too more!')
            break
        elif k == 0:
            print('k:', k)
            g_k = key2(x0)
            print('导数为：', g_k)
            d = -1 * g_k    #需保证为n*1向量
            theta = linear_search(x=x0, d=d, key=lambda p0, p1, p2: key1(p0, p1, p2))
            if theta == 0:
                break
            x1 = x0 + theta * d
            s_list.append(x1 - x0)
            y_list.append(key2(x1) - g_k)
            x0 = x1
            print('x1: ', x1)
            k += 1
            temp0 = key2(x0)
            g_k1_dis = np.dot(temp0, temp0)
            print('偏导数平方和: ', g_k1_dis)
            if g_k1_dis < threshold_value:
                print('g_k1_dis small enough! ', g_k1_dis)
                break
            del temp0, g_k, d, theta, x1
        else:
            g_k = key2(x0)
            print('k = ', k)
            print('导数为：', g_k)
            d = two_loop(s_list=s_list, y_list=y_list, g_k=g_k, k=k, m=m)
            print('d = ', d)
            theta = linear_search(x=x0, d=d, key=key1)
            if theta == 0:
                break
            x1 = x0 + theta * d
            s_list.append(x1 - x0)
            y_list.append(key2(x1) - g_k)
            x0 = x1
            print('x0: ', x0)
            k += 1
            temp0 = key2(x0)
            g_k1_dis = np.dot(temp0, temp0)
            print('偏导数平方和: ', g_k1_dis)
            if g_k1_dis < threshold_value:
                print('g_k1_dis small enough! ', g_k1_dis)
                break
            del temp0, g_k, d, theta, x1
    return x0