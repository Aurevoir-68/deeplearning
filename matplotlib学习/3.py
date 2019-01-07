# *_* coding:utf-8 *_*
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

x = range(11,31)
a1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
a2 = [1,0,3,1,2,2,3,3,2,1,2,1,1,1,1,1,1,1,1,1]
#设置图像大小
plt.figure(figsize=(8,6),dpi=100)

#设置刻度
plt.xticks(x, ['{}岁'.format(i) for i in range(11,31)], fontproperties=my_font)
plt.yticks(range(min(a1)-1,max(a1)+1))
#坐标标题
plt.xlabel('年龄', fontproperties=my_font)
plt.ylabel('女朋友数量', fontproperties=my_font)
plt.title('年龄和女朋友人数的关系', fontproperties=my_font)

#绘制网格
plt.grid()

plt.plot(x,a1, label='自己',color='orange',linestyle=':', linewidth=5, alpha=0.5)  # : - -. --
plt.plot(x,a2, label='同桌',color='cyan',linestyle='-', linewidth=1)

#添加图例
plt.legend(prop=my_font,loc='best')       # best, lower right, lower left, upper right, upper left

#展示
plt.show()