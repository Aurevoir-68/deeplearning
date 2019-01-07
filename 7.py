# *_* coding:utf-8 *_*
from matplotlib import pyplot as plt, font_manager

interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
quantity = [836, 2737, 3723, 3926, 3596, 1438, 3273, 642, 8824, 613, 215, 47]

my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

plt.figure(figsize=(20,8), dpi=100)

plt.bar(range(len(quantity)), quantity, width=1)

plt.xticks([i-0.5 for i in range(13)], interval+[150])

plt.grid(alpha=0.4)

plt.show()