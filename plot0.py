# -*- coding: utf-8 -*-
import numpy as np
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.animation import FuncAnimation
import matplotlib as mpl
np.set_printoptions(suppress=True)
from matplotlib.ticker import FuncFormatter
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体 SimHei为黑体
mpl.rcParams['axes.unicode_minus'] = False  # 用来正常显示负


def DrawGeoDtaabse():
  rcount = [
    [73.47, 76.48, 77.51, 81.93, 82.6, ],
    [89.87, 89.51, 91.59, 96.2, 92.12], ]

  y = ['16', '32']
  plt.xlabel("Patch size",fontsize = 16)  # X轴标签
  plt.ylabel("ASR",fontsize = 16)  # Y轴标签
  # plt.grid(True)   显示格网
  # plt.gcf().autofmt_xdate() 显示时间
  plt.tick_params(labelsize=16)
  plt.subplots_adjust(left=0.18, bottom=0.15)
  plt.rcParams.update({'font.size': 15})
  plt.legend(loc='upper right')
  plt.title("")  # 标题

  x1 = [10 ,22] # x轴点效率位置
  x2 = [i + 1 for i in x1]    # x轴线效率位置
  x3 = [i + 2 for i in x1]    # x轴线效率位置
  x4 = [i + 3 for i in x1]    # x轴线效率位置
  x5 = [i + 4 for i in x1]    # x轴线效率位置

  y1 = [i[0] for i in rcount] # y轴点效率位置
  y2 = [i[1] for i in rcount] # y轴线效率位置
  y3 = [i[2] for i in rcount] # y轴面效率位置
  y4 = [i[3] for i in rcount] # y轴线效率位置
  y5 = [i[4] for i in rcount] # y轴面效率位置
  # 占位以免 数据源标签丢失
  y0 = ["" ,"" ,]
  plt.bar(x1, y1, alpha=0.7, width=1, label="FPR=0",)
  plt.bar(x2, y2, alpha=0.7, width=1, label="FPR=1",)
  plt.bar(x3, y3, alpha=0.7, width=1, label="FPR=3", tick_label=y)
  plt.bar(x4, y4, alpha=0.7, width=1, label="FPR=5")
  plt.bar(x5, y5, alpha=0.7, width=1, label="FPR=10")

  def to_percent(temp, position):
    return '%1.0f' % (temp) + '%'
  plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
  plt.legend()
  plt.savefig('patch.png')
  plt.show()

def DrawGeoDtaabse0():
  rcount = [
    [0.46,1.11,0.61,12.42,30.02,],
    [0.32,3.21,28.06,47.71,66.62,],
    [0.18,70.9,92.02,94.82,96.9],
  ]

  y = [0.2, 0.3, 0.4]

  plt.xlabel("Blend ratio",fontsize = 16)  # X轴标签
  plt.ylabel("ASR",fontsize = 16)  # Y轴标签
  # plt.grid(True)   显示格网
  # plt.gcf().autofmt_xdate() 显示时间
  plt.tick_params(labelsize=16)
  plt.subplots_adjust(left=0.18, bottom=0.15)
  plt.legend() # 显示图例
  plt.title("")  # 标题

  x1 = [10, 16, 22] # x轴点效率位置
  x2 = [i + 1 for i in x1]    # x轴线效率位置
  x3 = [i + 2 for i in x1]    # x轴线效率位置
  x4 = [i + 3 for i in x1]    # x轴线效率位置
  x5 = [i + 4 for i in x1]    # x轴线效率位置

  y1 = [i[0] for i in rcount] # y轴点效率位置
  y2 = [i[1] for i in rcount] # y轴线效率位置
  y3 = [i[2] for i in rcount] # y轴面效率位置
  y4 = [i[3] for i in rcount] # y轴线效率位置
  y5 = [i[4] for i in rcount] # y轴面效率位置
  # 占位以免 数据源标签丢失
  y0 = ["" ,"" ,]
  plt.bar(x1, y1, alpha=0.7, width=1, label="LPR=0",)
  plt.bar(x2, y2, alpha=0.7, width=1, label="LPR=1",)
  plt.bar(x3, y3, alpha=0.7, width=1, label="LPR=3", tick_label=y)
  plt.bar(x4, y4, alpha=0.7, width=1, label="LPR=5")
  plt.bar(x5, y5, alpha=0.7, width=1, label="LPR=10")

  def to_percent(temp, position):
    return '%1.0f' % (temp) + '%'
  plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
  plt.legend()
  plt.savefig('blend.png')
  plt.show()

DrawGeoDtaabse()

DrawGeoDtaabse0()