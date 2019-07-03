#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random as rd
import math

rnd_50 = 0
rnd_45 = 0
rnd_40 = 0
rnd_35 = 0
rnd_30 = 0
rnd_25 = 0
rnd_20 = 0
rnd_15 = 0
rnd_10 = 0
rnd_05 = 0
rnd_00 = 0
rnd_005 = 0
rnd_010 = 0
rnd_015 = 0
rnd_020 = 0
rnd_025 = 0
rnd_030 = 0
rnd_035 = 0
rnd_040 = 0
rnd_045 = 0


def nor_rand():  # Box Muller
    nrm = 0
    for i in range(12):
        nrm += rd.random()  # rd.random

    return nrm - 6.0

def hisuto(num):
    global rnd_50
    global rnd_45
    global rnd_40
    global rnd_35
    global rnd_30
    global rnd_25
    global rnd_20
    global rnd_15
    global rnd_10
    global rnd_05
    global rnd_00
    global rnd_005
    global rnd_010
    global rnd_015
    global rnd_020
    global rnd_025
    global rnd_030
    global rnd_035
    global rnd_040
    global rnd_045
    if num < 5.0 and num >= 4.5:
        rnd_50 += 1
    if num < 4.5 and num >= 4.0:
        rnd_45 += 1
    if num < 4.0 and num >= 3.5:
        rnd_40 += 1
    if num < 3.5 and num >= 3.0:
        rnd_35 += 1
    if num < 3.0 and num >= 2.5:
        rnd_30 += 1
    if num < 2.5 and num >= 2.0:
        rnd_25 += 1
    if num < 2.0 and num >= 1.5:
        rnd_20 += 1
    if num < 1.5 and num >= 1.0:
        rnd_15 += 1
    if num < 1.0 and num >= 0.5:
        rnd_10 += 1
    if num < 0.5 and num >= 0.0:
        rnd_05 += 1
    if num < 0.0 and num >= -0.5:
        rnd_00 += 1
    if num < -0.5 and num >= -1.0:
        rnd_005 += 1
    if num < -1.0 and num >= -1.5:
        rnd_010 += 1
    if num < -1.5 and num >= -2.0:
        rnd_015 += 1
    if num < -2.0 and num >= -2.5:
        rnd_020 += 1
    if num < -2.5 and num >= -3.0:
        rnd_025 += 1
    if num < -3.0 and num >= -3.5:
        rnd_030 += 1
    if num < -3.5 and num >= -4.0:
        rnd_035 += 1
    if num < -4.0 and num >= -4.5:
        rnd_040 += 1
    if num < -4.5 and num >= -5.0:
        rnd_045 += 1
    sum = rnd_50 + rnd_45 + rnd_40 + rnd_35 + rnd_30 + rnd_25 + rnd_20 + rnd_15 + rnd_10 + rnd_05 + rnd_00 + rnd_005 + rnd_010 + rnd_015 + rnd_020 + rnd_025 + rnd_030 + rnd_035 + rnd_040 + rnd_045
    print(sum)
    print(rnd_50)
    print(rnd_45)
    print(rnd_40)
    print(rnd_35)
    print(rnd_30)
    print(rnd_25)
    print(rnd_20)
    print(rnd_15)
    print(rnd_10)
    print(rnd_05)
    print(rnd_00)
    print(rnd_005)
    print(rnd_010)
    print(rnd_015)
    print(rnd_020)
    print(rnd_025)
    print(rnd_030)
    print(rnd_035)
    print(rnd_040)
    print(rnd_045)

if __name__ == '__main__':
    rnd_list = []
    nnd_list = []
    ls_nd_list = []
    rnd_sum = 0
    nnd_sum = 0
    ls_nd_sum = 0
    rnd_deviation_sum = 0
    nnd_deviation_sum = 0
    ls_nd_deviation_sum = 0
    rnd_P = 0
    nnd_P = 0
    rnd_P51 = 0
    rnd_P52 = 0
    rnd_P53 = 0
    for i in range(1000000):
        rnd = nor_rand()
        nnd = rd.random()
        ls_nd = 256 * nor_rand() + 1024
        rnd_list.append(rnd)
        nnd_list.append(nnd)
        ls_nd_list.append(ls_nd)
        #hisuto(nnd)
        print(ls_nd)
        if rnd >= 0.3 and rnd <= 0.6:
            rnd_P += 1
        if nnd >= 0.3 and nnd <= 0.6:
            nnd_P += 1

        rnd_sum += rnd
        nnd_sum += nnd
        ls_nd_sum += ls_nd

    N = len(rnd_list)
    median1 = int(N/2) - 1
    median2 = int(N/2)
    median3 = int(median2/2)-1
    median4 = int(median2/2)
    median5 = median2 + median4
    median6 = median5 - 1
    rnd_list.sort()
    nnd_list.sort()
    rnd_median = (rnd_list[median1] + rnd_list[median2]) / 2
    nnd_median = (nnd_list[median1] + nnd_list[median2]) / 2
    rnd_itibuni = (rnd_list[median3] + rnd_list[median4]) / 2
    rnd_sanbuni = (rnd_list[median4] + rnd_list[median5]) / 2
    nnd_itibuni = (nnd_list[median3] + nnd_list[median4]) / 2
    nnd_sanbuni = (nnd_list[median4] + nnd_list[median5]) / 2
    rnd_ave = rnd_sum / N
    nnd_ave = nnd_sum / N
    ls_nd_ave = ls_nd_sum / N
    for i in range(1000000):
        rnd_deviation = rnd_list[i] - rnd_ave
        nnd_deviation = nnd_list[i] - nnd_ave
        ls_nd_deviation = ls_nd_list[i] - ls_nd_ave
        rnd_deviation_sum += (rnd_deviation * rnd_deviation)
        nnd_deviation_sum += (nnd_deviation * nnd_deviation)
        ls_nd_deviation_sum += (ls_nd_deviation * ls_nd_deviation)

    rnd_dispertion = rnd_deviation_sum / N
    nnd_dispertion = nnd_deviation_sum / N
    ls_nd_dispertion = ls_nd_deviation_sum / N
    rnd_dispertion_sqrt = math.sqrt(rnd_dispertion)
    nnd_dispertion_sqrt = math.sqrt(nnd_dispertion)
    ls_nd_dispertion_sqrt = math.sqrt(ls_nd_dispertion)

    for i in range(1000000):
        if rnd_list[i] >= (rnd_ave - rnd_dispertion_sqrt) and rnd_list[i] <= (rnd_ave + rnd_dispertion_sqrt):
            rnd_P51 += 1
        if rnd_list[i] >= (rnd_ave - 2 * rnd_dispertion_sqrt) and rnd_list[i] <= (rnd_ave + 2 *rnd_dispertion_sqrt):
            rnd_P52 += 1
        if rnd_list[i] >= (rnd_ave - 3 * rnd_dispertion_sqrt) and rnd_list[i] <= (rnd_ave + 3 * rnd_dispertion_sqrt):
            rnd_P53 += 1

    rnd_PP = rnd_P / N
    nnd_PP = nnd_P / N
    rnd_PP51 = rnd_P51 / N
    rnd_PP52 = rnd_P52 / N
    rnd_PP53 = rnd_P53 / N

    print('(1)')
    print('最大値:')
    print(max(rnd_list))
    print('最小値:')
    print(min(rnd_list))
    print('中央値:')
    print(rnd_median)
    print('第1四分位数:')
    print(rnd_itibuni)
    print('第3四分位数:')
    print(rnd_sanbuni)
    print('平均値:')
    print(rnd_ave)
    print("分散:")
    print(rnd_dispertion)
    print(rnd_dispertion_sqrt)
    print('\n(2)')
    print('最大値:')
    print(max(nnd_list))
    print('最小値:')
    print(min(nnd_list))
    print('中央値:')
    print(nnd_median)
    print('第1四分位数:')
    print(nnd_itibuni)
    print('第3四分位数:')
    print(nnd_sanbuni)
    print('平均値:')
    print(nnd_ave)
    print("分散:")
    print(nnd_dispertion)
    print('\n(3)')
    print('平均:')
    print(ls_nd_ave)
    print('分散:')
    print(ls_nd_dispertion)
    print('\n(4)')
    print('P(0.3 <= rnd <= 0.6):')
    print(rnd_PP)
    print('P(0.3 <= nnd <= 0.6):')
    print(nnd_PP)
    print('\n(5)')
    print('P(μ - σ <= rnd <= μ + σ):')
    print(rnd_PP51)
    print('P(μ - 2σ <= rnd <= μ + 2σ):')
    print(rnd_PP52)
    print('P(μ - 3σ <= rnd <= μ + 3σ):')
    print(rnd_PP53)

