# 绘图，如折线、饼图、柱形图等
import matplotlib.pyplot as plt
import numpy as np


def pyplot_t():
    x = np.array([0, 6])
    y = np.array([0, 100])
    plt.plot(x, y)
    plt.plot(x, y, 'o')  # o 表示只绘制坐标点
    plt.show()


if __name__ == "__main__":
    pyplot_t()
