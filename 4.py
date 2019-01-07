# *_* coding:utf-8 *_*
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')
y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1,32)
x_10 = range(51,82)

#设置图像大小
plt.figure(figsize=(8,6),dpi=100)

plt.scatter(x_3, y_3,label='3月份')
plt.scatter(x_10, y_3, label='10月份')

#调整x轴的刻度
x3_tick = ['3月{}号'.format(i) for i in x_3]
x10_tick = ['10月{}号'.format(i-50) for i in x_10]
plt.xticks((list(x_3)+list(x_10))[::2], (list(x10_tick)+list(x3_tick))[::2], rotation=45, fontproperties=my_font)

#添加描述信息
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度', fontproperties=my_font)
plt.title('标题', fontproperties=my_font)

plt.legend(prop=my_font)

plt.show()