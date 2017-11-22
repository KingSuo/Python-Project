# -*- coding: utf-8 -*-
"""
# @Author: KingSuo
# @File: CalculateBGRMeans.py                                                                
# @Time: 2017/11/18                           
# @Contact: 648230502@qq.com
# @blog:
# @Description: 
"""

import numpy as np

def calculate_bgr_means(hough_detect_frame):
    """
    
    :param hough_detect_frame:霍夫检测返回的只包含圆的cimg（frame） 
    :return: 该frame中的bgr均值（list）
    """
    b_layer = hough_detect_frame[0:len(hough_detect_frame), 0:len(hough_detect_frame[0]), 0:1]
    g_layer = hough_detect_frame[0:len(hough_detect_frame), 0:len(hough_detect_frame[0]), 1:2]
    r_layer = hough_detect_frame[0:len(hough_detect_frame), 0:len(hough_detect_frame[0]), 2:3]
    b_mean = (b_layer.sum() - b_layer.max() - b_layer.min()) / (np.count_nonzero(b_layer) - 2)
    g_mean = (g_layer.sum() - g_layer.max() - g_layer.min()) / (np.count_nonzero(g_layer) - 2)
    r_mean = (r_layer.sum() - r_layer.max() - r_layer.min()) / (np.count_nonzero(r_layer) - 2)
    bgr_mean_list = [b_mean, g_mean, r_mean]

    return bgr_mean_list