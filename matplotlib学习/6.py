# *_* coding:utf-8 *_*
from matplotlib import pyplot as plt, font_manager

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

#准备数据
a=['猩球崛起3:终极之战','敦刻尔克','蜘蛛侠:英雄归来','战狼2']
b_16=[15746,312,4497,319]
b_15=[12357,156,2045,168]
b_14=[2358,399,2358,362]

#设置图像大小
plt.figure(figsize=(8,6),dpi=100)

#刻度
plt.xticks([i+0.3 for i in range(len(a))], a, fontproperties=my_font)

#绘图
plt.bar(range(len(a)),b_14,width=0.2, label='14号')
plt.bar([i+0.2 for i in range(len(a))],b_15,width=0.2, label='15号')
plt.bar([i+0.4 for i in range(len(a))],b_16,width=0.2, label='15号')


plt.legend(prop=my_font)
#展示
plt.show()