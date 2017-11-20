# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: Select_Fun.py                                                                
# @Time: 2017/10/23                                   
# @Contact: 648230502@qq.com
# @blog: 
# @Description:选择函数 
"""
import numpy as np
from collections import Counter

def select_fun(population_fitness_dict, isEliteSelect=0):
    """             
    :param population_fitness_dict:种群适应度字典
    :param isEliteSelect: 是否进行精英选择（bool）
    :return: 父代染色体列表（list）
    """
    #population_fitness_sorted_array_temp:种群各个染色体适应度按照由小到大顺序拍好的由键组成的数组(array)
    population_fitness_sorted_array_temp = np.array(sorted(population_fitness_dict))
    population_fitness_dict_temp = dict(population_fitness_dict)
    parent_chromosomes_list = [0, 0]    #定义父代染色体列表
    #temp0:所有染色体适应度的比重(array)
    temp0 = population_fitness_sorted_array_temp / sum(population_fitness_sorted_array_temp)

    iteration_upper_bound = 0
    while(parent_chromosomes_list[0] == parent_chromosomes_list[1]):    #当选出来的两个染色体是同一个染色体时则执行while循环
        if iteration_upper_bound > 10:
            print('iteration_upper_bound: ', iteration_upper_bound)
            parent_chromosomes_list[0] = population_fitness_dict_temp[list((population_fitness_dict_temp).keys())[0]]
            parent_chromosomes_list[1] = population_fitness_dict_temp[list(population_fitness_dict_temp.keys())[1]]

        #将所有染色体的适应度按照大小置于轮盘上
        temp1 = [0]     #定义存储染色体适应度按照比重分布的列表（list）形如：[0, 0.02, ...., 1]
        for i in range(len(temp0)):
            temp1.append(sum(temp0[:(i + 1)]))  #将染色体适应度比重按照所有比重之和为一置于0—1的概率区间上
        select_number = 2
        if isEliteSelect:   #如果进行精英选择规则，那么只需挑选出一个待确定父代， 即parent_chromosomes_list[1]已确定
            select_number = 1
            parent_chromosomes_list[1] = population_fitness_dict_temp[max(population_fitness_sorted_array_temp)]
        for j in range(select_number):
            temp2 = sorted(np.random.random(10))    #产生10个0-1之间的随机数并按照大小拍序,然后选择出落在轮盘同一区域次数最多的那个区域表示的染色体数值
            temp3 = []
            for m in temp2:
                for k in range(len(temp1) - 1):
                    if temp1[k] < m and temp1[k + 1] > m:
                        temp3.append(k)
                        break
            temp3_counter = Counter(temp3)
            print(temp3_counter)
            for i in temp3_counter:
                if temp3_counter[i] == max(temp3_counter.values()):     #找出出现次数最大的那一项
                    parent_chromosomes_list[j] = population_fitness_dict_temp[population_fitness_sorted_array_temp[i]]
                    break
        iteration_upper_bound += 1
        print('parent_chromosomes_list: ', parent_chromosomes_list)
    print('population_fitness_sorted_array_temp: ', population_fitness_sorted_array_temp)
    print('population_fitness_dict_temp: ', population_fitness_dict_temp)
    return parent_chromosomes_list

# select_fun({12: 45, 23: 443, 31: 54, 421: 34, 564: 65}, isEliteSelect=0)