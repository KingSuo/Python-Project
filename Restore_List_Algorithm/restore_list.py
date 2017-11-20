# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: restore_list.py                                                                
# @Time: 2017/10/16                                   
# @Contact: 648230502@qq.com
# @Description: 

问题：
    已知有n个房间，每个房间里人数不知（有的房间可能没人）。现对房间人数重新分配，分配规则为指定第i个房间，将其中所有人员从下
一个房间开始一个一个分配到相应房间中去，直至人员分配结束。
现已知分配结束之后的各个房间人数，以及最后一个人被分配到的房间。设计算法求出原来每个房间的人员数及指定的被抽出的房间号。
问题重述：
    设A为list，A = [x0,x1,x2,...,xn-1],从A的第i个位置中抽出数字A[i],并将其从第i+1位开始向下一个一个循环分配，
即A'[i+1] = A[i+1] + 1, A'[i+2] = A[i+2] + 1....。
    已知，A'= [x0', x1',...,xn-1']，以及最后一个数加在第k位上，求A。
算法思路：
    对于被取出来的那一位（记为i），其在分配后value应为最小值；如果A[i]' = 0，即说明A[i] < len(A);如果A[i]' >= 1,即说明
A[i] >= len(A)。找出i值，再分不同情况求出A[i]值；还原A：A - min（A），求补偿值，替换A[i] = A[i]
"""
def restore_list(a_list, end_position_int):
    """
        
    :param a_lsit: 
    :param position_int: 
    :return: 
    """
    import numpy as np
    a_last = np.array(a_list).astype(int)
    a_min = min(a_last)
    index = 0
    index_list = []
    for i in a_last:
        if i == a_min:
            index_list.append(index)
        index += 1
    if end_position_int < index_list[0]:
        start_position_int = index_list[len(index_list) - 1]
        compensate_value = end_position_int + len(index_list) - start_position_int
        extent_list = list(range(0, end_position_int + 1)) + list(range(start_position_int, len(a_last)))
    elif end_position_int >= index_list[len(index_list) - 1]:
        start_position_int = index_list[len(index_list) - 1]
        compensate_value = end_position_int - start_position_int
        extent_list = list(range(start_position_int, end_position_int + 1))
    for i in range(len(index_list) - 1):
        if index_list[i] <= end_position_int and index_list[i + 1] > end_position_int:
            start_position_int = index_list[i]
            compensate_value = end_position_int - start_position_int
            extent_list = list(range(start_position_int, end_position_int + 1))

    a_start_value = a_min * len(a_last) + compensate_value

    a_before = a_last - a_min
    for i in extent_list:
        a_before[i] = a_before[i] - 1
    a_before[start_position_int] = a_start_value
    print('被选位置：', start_position_int)
    print('调整前：', a_before)

    return start_position_int, a_before

restore_list([115, 46, 98, 46, 113, 46, 987, 46, 98, 65], 3)