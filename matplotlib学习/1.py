# *_* coding:utf-8 *_*
from matplotlib import pyplot as plt

x = range(2,17)
y = [73.64,78,80.28,81.66,82.54,83.59,85.04,85.19,86.47,87.14,87.83,88.08,88.25,88.80,89.03]

plt.figure(figsize=(8,6),dpi=100)
plt.xticks(range(0,20))
#plt.yticks([i+2 for i in range(71,91,2)])
plt.yticks(range(int(min(y)-3),int(max(y)+2)))
plt.plot(x,y)
plt.xlabel('Anchor box')
plt.ylabel('Average IOU%')
plt.show()