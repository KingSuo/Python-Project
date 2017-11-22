import numpy as np
from Linear_Search_Algorithm import linear_search
from L_BFGS_Algorithm import L_BFGS

#Linear_Search_Algorithm Test
# x = [10, -3, 5]
# d = [-2, 3, -10]
# theta = linear_search(x, d, key=lambda p0, p1, p2: np.dot((p0 + p1 * p2), [1, 1, 1]))
# print(theta)
#Linear_Search_Algorithm Test

#L_BFGS_Algorithm Test1
# 求函数z = x1**2 + x2**2 + x1*x2最值
#初始值为 x0 = [-56100, 12052]
#迭代次数：12
#输出结果：g_k1 small enough!  1.30895547056e-16
#          x0:  [ 3.34002044e-09  -7.37978060e-09]
# x0 = [-56100, 12052]
# x = L_BFGS(x_0=x0, threshold_value=0.00000000001, m=10,\
#            key1=lambda p0, p1, p2: np.dot((p0 + p1 * p2), (p0 + p1 * p2))\
#                                    + np.dot((p0 + p1 * p2), [1, 0]) * np.dot((p0 + p1 * p2), [0, 1]),\
#            key2=lambda p: np.array([np.dot(p, [2, 1]), np.dot(p, [1, 2])]))
#L_BFGS_Algorithm Test1
#######################

#L_BFGS_Algorithm Test2
# 求函数z = x1**2* x2**2 * x1+ x1 + x2最值
#初始值为x0=[-3, 2]时
#迭代次数：37
#输出结果：min value: -2.83722071003
#          x0:  [ 0.0358784  -2.88380438]
# x0 = [-3, 2]
# x = L_BFGS(x_0=x0, threshold_value=0.00000001,\
#            key1=lambda p0, p1, p2: (np.dot((p0 + p1 * p2), [1, 0]) ** 2) * (np.dot((p0 + p1 * p2), [0, 1]) ** 2)\
#            + np.dot((p0 + p1 * p2), [1, 0]) + np.dot((p0 + p1 * p2), [0, 1]),
#            key2=lambda p: np.array([2 * np.dot(p, [1, 0]) * np.dot(p, [0, 1]) ** 2\
#                                     + 1, 2 * np.dot(p, [0, 1]) * np.dot(p, [1, 0]) ** 2 + 1]))
#L_BFGS_Algorithm Test2
#######################

#L_BFGS_Algorithm Test3
# 求函数z = x1**2 + x2**2 + x1*x2最值
#初始值为 x0 = [506, -102]
#迭代次数：12
#输出结果：g_k1 small enough!  7.08789309015e-17
#          x0:  [ -2.86418891e-09  -1.05864859e-09]
x0 = [506, -102]
x = L_BFGS(x_0=x0, threshold_value=0.00000000001, m=10,\
           key1=lambda p0, p1, p2: np.dot((p0 + p1 * p2), (p0 + p1 * p2))\
                                   + np.dot((p0 + p1 * p2), [1, 0]) * np.dot((p0 + p1 * p2), [0, 1]),\
           key2=lambda p: np.array([np.dot(p, [2, 1]), np.dot(p, [1, 2])]))
#L_BFGS_Algorithm Test3
#######################
