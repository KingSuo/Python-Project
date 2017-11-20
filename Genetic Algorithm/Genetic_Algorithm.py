# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: Genetic_Algorithm.py                                                                
# @Time: 2017/10/23                                   
# @Contact: 648230502@qq.com
# @blog: 
# @Description:遗传算法 
"""

from Initialize_Fun import initialize_fun
from Decode_Fun import decode_fun
from Fitness_Fun import fitness_fun
from Select_Fun import select_fun
from Crossover_Fun import crossover_fun
from Mutate_Fun import mutate_fun
from StopRule_Fun import stopRule_fun

def genetic_algorithm(population_size=50, chromosome_length=17, lower_bound=0, upper_bound=9, fitness_change_rate=9999,\
                      minFitness_change_rate=0.000000001, key1=None, isEliteSelect=0, maxIterate_times=20):
    k = 0
    population_list = initialize_fun(population_size=population_size, chromosome_length=chromosome_length)
    while(stopRule_fun(iterate_times=k, fitness_change_rate=fitness_change_rate, \
                       minFitness_change_rate=minFitness_change_rate, maxIterate_times=maxIterate_times)):
        new_population_list = []
        #求种群适应度
        population_fitness_dict = fitness_fun(population_list=population_list, chromosome_length=chromosome_length, \
                                              lower_bound=lower_bound, upper_bound=upper_bound, key=key1)
        maxFitness_old = max(population_fitness_dict)
        while(len(new_population_list) < population_size):
            # population_fitness_dict = fitness_fun(population_list=population_list, chromosome_length=chromosome_length,\
            #                                       lower_bound=lower_bound, upper_bound=upper_bound, key=key1)
            #选择父代染色体
            parent_chromosomes_list = select_fun(population_fitness_dict=population_fitness_dict, \
                                                 isEliteSelect=isEliteSelect)
            #获得子代交叉染色体
            son_cross_chromosome_list = crossover_fun(parent_chromosomes_list=parent_chromosomes_list)
            #获得子代变异染色体
            son_mutate_chromosome_list = mutate_fun(son_chromosomes_list=son_cross_chromosome_list)
            #将新获得的染色体添加到种群中
            new_population_list.append(son_mutate_chromosome_list[0])
            new_population_list.append(son_mutate_chromosome_list[1])
        population_list = new_population_list
        population_fitness_dict = fitness_fun(population_list=population_list, chromosome_length=chromosome_length, \
                                              lower_bound=lower_bound, upper_bound=upper_bound, key=key1)
        trueValue_list = [decode_fun(i, chromosome_length=chromosome_length, lower_bound=lower_bound, upper_bound=upper_bound) for i in population_list]
        print('trueValue_list: ', trueValue_list)
        print('population_fitness: ', sorted(population_fitness_dict))
        print('k: ', k)
        k += 1
        maxFitness_new = max(population_fitness_dict)
        fitness_change_rate = maxFitness_new - maxFitness_old
    x = decode_fun(population_fitness_dict[max(population_fitness_dict)])
    print('x = ', x)
    print('max value = ', maxFitness_new)

    return x