import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator
plt.rcParams['font.family']='SimHei'
from matplotlib.ticker import FuncFormatter
x = [0.2,0.3,0.4]
y1 = [0.46, 0.32, 0.18]
y2 = [1.11, 3.21, 70.9]
y3 = [0.61, 28.06, 92.02]
y4 = [12.42, 47.71, 94.82]
y5 = [30.02, 66.62, 96.9]

# x = [16,32]
# y1 = [73.47,89.87]
# y2 = [76.48, 89.51]
# y3 = [77.51, 91.59]
# y4 = [81.93, 96.2]
# y5 = [82.6, 92.12]

plt.plot(x, y1, 'p-',label="LPR=0")
plt.plot(x, y2, 'o-',label="LPR=1")
plt.plot(x, y3, 'x-',label="LPR=3")
plt.plot(x, y4, '^-',label="LPR=5")
plt.plot(x, y5, '*-',label="LPR=10")

plt.ylim(0, 100)
# plt.xlabel("α")#横坐标名字
plt.xlabel("Patch Size", fontsize = 13)#横坐标名字
plt.ylabel('ASR', fontsize = 13)#纵坐标名字
plt.tick_params(labelsize=13)
# plt.tight_layout()
plt.subplots_adjust(left=0.18, bottom=0.15)
plt.legend(loc="best")

#把x轴的刻度间隔设置为1，并存在变量里
# x_major_locator=MultipleLocator(1)

#ax为两条坐标轴的实例
ax=plt.gca()

#把x轴的主刻度设置为1的倍数
# ax.xaxis.set_major_locator(x_major_locator)
plt.xticks(x,x[::1])
def to_percent(temp, position):
  return '%1.0f'%(temp) + '%'
plt.gca().yaxis.set_major_formatter(FuncFormatter(to_percent))
# plt.gca().xaxis.set_major_formatter(FuncFormatter(to_percent))
plt.savefig('2.png')
plt.show()

