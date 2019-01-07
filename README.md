#### matplotlib绘制步骤：

1.实例化字体
 my_font = font_manager.FontProperties(fname='/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc')

2.准备数据
 x = range(0,120)
 y = [random.randint(20,35) for i in range(120)]

3.设置图像大小
 plt.figure(figsize=(8,6),dpi=100)

4.对刻度进行设置
 plt.xticks(list(x)[::3],(x_tick1+x_tick2)[::3],rotation=45,fontproperties=my_font)
 plt.xlabel('时间', fontproperties=my_font)
 plt.ylabel('温度', fontproperties=my_font)
 plt.title('温度和时间的关系', fontproperties=my_font)

5.绘制图像
 plt.plot(x,y)

6.设置网格
 plt.grid()              #参数：alpha

7.设置图例
 plt.legend()            #参数：alpha prop loc

8.展示
 plt.show()
