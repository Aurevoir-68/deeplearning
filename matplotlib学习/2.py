# *_* coding:utf-8 *_*
from matplotlib import pyplot as plt
import random
from matplotlib import font_manager

# font = {'family': 'Microsoft YaHei',
#         'weight': 'bold',
#        }
# matplotlib.rc('font', **font)

#实例化
my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

#选择数据
x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

#绘制数据
plt.figure(figsize=(20,8),dpi=100)
x_tick1 = ['10点{}分'.format(i) for i in range(60)]
x_tick2 = ['11点{}分'.format(i) for i in range(60)]

#对刻度进行设置
plt.xticks(list(x)[::3],(x_tick1+x_tick2)[::3],rotation=45,fontproperties=my_font)
plt.xlabel('时间', fontproperties=my_font)
plt.ylabel('温度', fontproperties=my_font)
plt.title('温度和时间的关系', fontproperties=my_font)
plt.plot(x,y)

#展示
plt.show()