# -*- coding: utf-8 -*-
"""
#注意：在一开始编写算法时，使用下面的zeta_list列表代替两个for 循环中的alpha及beta求解的部分因子，导致算法无法收敛，寻找
#良久才发现问题所在一开始这样写的目的是为了减少运算量，不曾注意到zeta_list的元素可能会出现极小情况，导致alpha接近0，进而
#使q接近不变，再次循环时又会出现同样问题。故作此记录以备忘！！！
# zeta_list = [1 / np.dot(np.array(y_list_temp[i]), s_list_temp[i]) for i in second_loop_area_list]    #保留最新，元素为常数

# @Author: KingSuo
# @File: Two_Loop_Recursion.py                                                                
# @Time: 2017/10/30                             
# @Contact: 648230502@qq.com
# @Description:两循环算法 
#参考Wiki百科：https://en.wikipedia.org/wiki/Limited-memory_BFGS

two-loop recursion 算法可以方便地求出下降方向d
"""
import numpy as np


def two_loop(s_list, y_list, g_k, k, m=3):
    """
    
    :param s_list: 传入s列表，其中元素为s_i= x_i+1 - x_i，i取0,1...k-1，k为第k次迭代
    :param y_list: 传入y列表，其中元素为y_i= g_i+1 - g_i，i取0,1...k-1，k为第k次迭代
    :param g_k: x = x_k-1时的函数导数（梯度值）
    :param k: 第k次迭代
    :param m: 预保留的（s，y）对个数
    :return: 函数搜索方向梯度d
    """
    upper_limit = min(k, m)     #保留个数上限值
    offset = max(0, k - m)  #定义补偿值
    q = -np.array(g_k)   #传入第k-1次导数，即上一次求得的x值的函数值导数；array类型，shape = （n, ），其中n为变量个数
    s_list_temp = list(s_list)  #另存s列表
    y_list_temp = list(y_list)  #另存y列表
    alpha = [0 for _ in range(upper_limit)]   #定义alpha的长度：最大不超过预保留的长度m
    beta = [0 for _ in range(upper_limit)]  # 定义beta的长度：最大不超过预保留的长度m
    first_loop_area_list = [k - i for i in range(1, m + 1) if k - i >= 0]   #第一个循环遍历列表
    second_loop_area_list = [k - i for i in range(m + 1, 0, -1) if k - i >= 0]   #第er个循环遍历列表

    #此处不能使用下面写法
    # zeta_list = [1 / np.dot(np.array(y_list_temp[i]), s_list_temp[i]) for i in second_loop_area_list]    #保留最新，元素为常数

    # 第一个循环
    for i in first_loop_area_list:
        j = i - offset
        alpha[j] = np.dot(s_list_temp[i], q) / np.dot(y_list_temp[i], s_list_temp[i])
        q = q - alpha[j] * y_list_temp[i]   #为向量,array类型，shape = （n，），其中n为变量个数

    Hessian = np.dot(np.matrix(y_list_temp[k - 1]).T, np.matrix(s_list_temp[k - 1])) / np.dot(y_list_temp[k - 1], y_list_temp[k - 1])      #矩阵，matrix类型，shape = （n, n），其中n为变量个数

    z_matrix = np.dot(Hessian, np.matrix(q).T)     #为矩阵，matrix类型，shape = （n, 1），其中n为变量个数
    z = np.array([i[0, 0] for i in z_matrix])     #为向量，array类型, shape = (n, )，其中n为变量个数

    # 第二个循环
    for i in second_loop_area_list:
        j = i - offset
        beta[j] = np.dot(y_list_temp[i], z) / np.dot(y_list_temp[i], s_list_temp[i])
        z += s_list_temp[i] * (alpha[j] - beta[j])   #为向量，array类型，shape= （n， ），其中n为变量个数

    #释放内存
    del s_list_temp, y_list_temp, alpha, beta, Hessian, q

    return z