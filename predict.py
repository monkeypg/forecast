#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression

if len(sys.argv) != 10:
    print("Usage: " + sys.argv[0] + " 購買人數 銷售冊數 HQ TL BL teens girl novel_love other")
    sys.exit("Example: " + sys.argv[0] + " 7663 127358 85 1796 628 220 274 5409 2552")

# x = 購買人數, 銷售冊數, HQ, TL, BL, teens, girl, novel_love, other
X = np.array([
[7663,  127358, 85,     1762,   608,    220,    266,    5361,   2496],
[7556,  133463, 80,     1683,   555,    219,    249,    5263,   2391],
[7649,  129021, 75,     1594,   518,    204,    229,    5165,   2257],
[7708,  137559, 70,     1516,   485,    188,    215,    5088,   2139],
[7151,  131765, 65,     1427,   452,    182,    206,    5001,   2036],
[6390,  114068, 60,     1346,   424,    178,    198,    4932,   1958],
[5154,  87930,58,       1256,   398,    173,    185,    4871,   1884],
[4665,  80548,53,       1169,   371,    173,    165,    4830,   1828],
[3582,  55164,50,       1072,   349,    172,    158,    4797,   1740],
[3065,  48052,45,       991,    328,    172,    150,    4766,   1660],
[2863,  46684,37,       936,    305,    169,    137,    4734,   1575],
[2864,  43608,35,       894,    277,    158,    122,    4703,   1490],
[3050,  43111,30,       844,    248,    150,    120,    4675,   1422],
[2958,  45410,25,       791,    223,    140,    116,    4633,   1347],
[2941,  44716,20,       731,    205,    132,    113,    4594,   1282],
[3095,  44130,15,       683,    189,    124,    108,    4558,   1210],
[3486,  50069,10,       626,    166,    113,    107,    4512,   1125],
[3125,  43645,5,        583,    147,    108,    106,    4485,   1079],
[2589,  31988,0,        554,    114,    104,    101,    4449,   1021],
[2119,  31238,0,        508,    111,    93,         90, 4362,   914],
[2848,  39569,0,        471,    111,    92,         66, 4271,   834],
[2748,  34197,0,        425,    109,    89,         60, 4165,   759],
[2969,  37364,0,        383,    103,    88,         54, 4064,   692],
[2754,  34830,0,        339,    103,    88,         48, 3935,   685],
[2438,  29846,0,        303,    102,    87,     43,     3815,   596],
[2368,  29020,0,        275,    101,    83,     40,     3700,   561],
[1995,  24314,0,        257,    101,    74,     38,     3596,   559],
[2028,  26797,0,        244,    99,         65, 37,     3480,   555],
[1652,  19137,0,        219,    99,         49, 37,     3371,   550],
[808,   10684,0,        206,    92,         37, 37,     3273,   549],
[721,   7793,0, 182,    83,         31, 37,     2413,   545],
[553,   6467,0, 148,    70,         22, 37,     2413,   540],
[453,   5415,0, 117,    68,         16, 35,     2413,   539],
[416,   4879,0, 95,         68,     15, 35,     2413,   539],
[387,   3833,0, 83,         63,     12, 35,     2413,   539],
[416,   3725,0, 70,         53,     10, 30,     2413,   539],
[118,   1160,0, 57,         39,     10, 30,     2413,   480],
[88,    712,0,  36,         31,     0,  30,     2413,   480],
[54,    411,0,  36,         31,     0,  30,     1139,   478],
[35,    289,0,  14,         6,      0,  23,     1139,   478],
[38,    244,0,  14,         6,      0,  23,     0,      0],
[41,    237,0,  14,         6,      0,  23,     0,      0]
])
# y = 銷售總額
y = np.array([
4145840,
4517700,
4607510,
5142580,
5028100,
4159050,
3130680,
2923780,
2001000,
1771200,
1701280,
1603500,
1571880,
1519010,
1491170,
1500730,
1609180,
1397990,
1030720,
933290,
1207190,
1047550,
1109840,
996210,
799080,
805920,
652800,
752300,
558610,
306930,
200540,
154260,
134940,
125080,
99570,
91480,
26770,
17830,
12660,
7700,
7360,
6780])

lm = LinearRegression()
lm.fit(X, y)

# 預計(購買人數, 銷售冊數, HQ, TL, BL, teens, girl, novel_love, other)
to_be_predicted = np.array([
    [int(sys.argv[1]), int(sys.argv[2]),int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6]), int(sys.argv[7]), int(sys.argv[8]), int(sys.argv[9])]
])
predicted_sales = lm.predict(to_be_predicted)

# 預測新銷售總額
#print(predicted_sales) #結果:4426029.06686106

# 模型績效
mse = np.mean((lm.predict(X) - y) ** 2)
r_squared = lm.score(X, y)
adj_r_squared = r_squared - (1 - r_squared) * (X.shape[1] / (X.shape[0] - X.shape[1] - 1))

# 印出模型績效
#print(mse) #結果:22156691089.6
#print(r_squared) #結果:0.990078637189
#print(adj_r_squared) #結果:0.990078637189

# 印出 p-value
#print(f_regression(X, y)[1])
#結果:[  3.92672977e-30   2.85515704e-19   8.51000083e-24   1.88425066e-22    3.84816292e-15   3.83712394e-22   2.36611570e-08   2.97031473e-19]

result = {"sales": predicted_sales[0], "mse": mse, "r_squared": r_squared, "adj_r_squared": adj_r_squared, "p_value": f_regression(X, y)[1].tolist()}
print(json.dumps(result))
