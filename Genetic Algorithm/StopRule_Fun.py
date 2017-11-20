# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: StopRule_Fun.py                                                                
# @Time: 2017/10/23                                   
# @Contact: 648230502@qq.com
# @blog: 
# @Description: 终止函数
"""
def stopRule_fun(iterate_times, fitness_change_rate=9999, minFitness_change_rate=0.0000001, maxIterate_times=20):
    print('fitness_change_rate: ', fitness_change_rate)
    if iterate_times >= maxIterate_times:
        print('Iterate times too many!', iterate_times)
        return False
    elif fitness_change_rate <= minFitness_change_rate:
        print('Change not enough!', fitness_change_rate)
        return False
    else:
        return True
