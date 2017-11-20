# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: test.py                                                                
# @Time: 2017/10/23                                   
# @Contact: 648230502@qq.com
# @blog: 
# @Description:测试 求解函数 f(x) = x + 10*sin(5*x) + 7*cos(4*x) 在区间[0,9]的最大值。
"""
from numpy import sin, cos
from Genetic_Algorithm import genetic_algorithm

#test1
# genetic_algorithm(key1=lambda p: p + 10 * sin(5 * p) + 7 * cos(4 * p), maxIterate_times=300, isEliteSelect=1)
#output result:
# trueValue_list:  [7.223909178994591, 3.3564175141717083, 3.216203431727842, 7.856451846709035, 7.85686383715696, \
#                   7.707036644261507, 7.707311304560124, 7.856589176858344, 7.854254564320101, 7.7861388102631395, \
#                   7.15352747747404, 7.821295328486087, 5.606434680440372, 8.980636448947516, 7.611317530193559,\
#                   7.847800047302607, 7.646474048416507, 7.811407557735883, 7.852812597752362, 8.840834356951575,\
#                   7.852057281931167, 5.46580860754858, 5.606846670888297, 7.750982292040192, 6.696630070725027, \
#                   7.847662717153298, 8.911422053696088, 7.874030105820509, 2.196664403262354, 3.3564175141717083,\
#                   7.85686383715696, 7.856726507007652, 8.911422053696088, 3.3564175141717083, 7.847662717153298, \
#                   7.874579426417743, 7.575474361224069, 7.289552990364001, 7.713903151726926, 7.855284540439913, \
#                   7.787100121308298, 7.680669255594296, 8.99903868895484, 7.857001167306269, 7.874442096268434, \
#                   5.325182534656789, 7.845740095062981, 7.854254564320101, 7.641530163041405, 8.981460429843366]
# population_fitness:  [-13.130756343263652, -6.4993141373862064, -6.4557443155254042, -0.82820595361850735, \
#                       -0.08149369394510142, 0.75373067993153864, 1.6649633951382325, 1.9609555452097673, \
#                       2.8952076308005399, 4.1829737370587372, 6.9817053581434454, 7.0030787586723378, \
#                       7.6600841771213606, 12.446336796162273, 14.905831466616666, 15.560045704514094, \
#                       15.576112015919843, 19.085717250867759, 21.189712135666174, 21.342093645044649, \
#                       21.381375500076206, 21.391165432178916, 21.394426025390665, 21.417212098801389, \
#                       21.426957141025483, 23.967025687405357, 24.366677892589081, 24.633535307418349, \
#                       24.801332862690341, 24.803875877377529, 24.805537231467085, 24.841325344981826, \
#                       24.851839356315253, 24.854474950800874, 24.854581644756458, 24.854860763917888, \
#                       24.855012707963798, 24.855137343926927, 24.855347406062741]

genetic_algorithm(key1=lambda p: p + 10 * sin(5 * p) + 7 * cos(4 * p), maxIterate_times=50, isEliteSelect=1)

#0-9上求解最大值结果
# k=5
# Change not enough! 0.0
# x =  7.857619152978156
# max value =  24.8552243021