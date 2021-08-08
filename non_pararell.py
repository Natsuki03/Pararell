# -*- coding: utf-8 -*-

# 逐次処理

import time
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp

def julia(max, comp):
    re, im = comp[0], comp[1]
    #実部が-0.7、虚部が-0.3の複素数cを作成(ここの数値を変えればさまざまなジュリア集合を作れる)
    c = complex(-0.7, -0.3)

    #実部がre、虚部がimの複素数zを作成
    z = complex(re, im)

    for i in range(max):
        z = z*z + c
        #zの絶対値が一度でも2を超えればzが発散することを利用
        if abs(z) >= 2:
            return i        #発散する場合には何回目のループで終わったかを返す
    return max     #無限大に発散しない場合にはmaxを返す

re = np.linspace(-2, 2, 2000)
im = np.linspace(2, -2, 2000)

#実部と虚部の組み合わせを作成
Re, Im = np.meshgrid(re, im)
comp = np.c_[Re.ravel(), Im.ravel()]

#計算結果を格納するための零行列を作成
Julia = np.zeros(len(comp))

s_time = time.time()
#マンデルブロ集合に属するかの計算(ここを並列化)
for i, c_point in enumerate(comp):
    Julia[i] = julia(200, c_point)

e_time = time.time()
print("time: {0:.3f}[s]".format(e_time - s_time))

Julia = Julia.reshape((2000, 2000))

#画像生成
fig = plt.figure(dpi=600)
plt.axis("off")
plt.imshow(Julia, cmap="bone", extent=[-2, 2, -2, 2])
fig.set_size_inches(1.5, 1.5)
plt.show()

#画像を保存
fig.savefig("julia.png")