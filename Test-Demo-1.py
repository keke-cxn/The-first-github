# 导入 matplotlib.pyplot和numpy分别命名plt和np
import matplotlib.pyplot as plt
import numpy as np 
# linspace 第一个参数序列起始值, 第二个参数序列结束值,第三个参数为样本数默认50
# 设置0到3PI的序列，精度为100
x = np.linspace(0, 3 * np.pi, 100)
# 设置正弦函数
y = np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei'] #加上这一句就能在图表中显示中文
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# 开辟空间 一行两列 中第一列
plt.subplot(1,2,1)
# 设置标题
plt.title(r'$f(x)=sin(x)$') 
# 生成图像函数
plt.plot(x, y)
# plt.show()


# 设置x1为 t*3/8*PI w=3/8*PI 
# t的值是x序列中的每一个值 x1其实就是频谱的横坐标
x1 = [t*0.375*np.pi for t in x]
# 生成频谱
y1 = np.sin(x1)
# 开辟空间 一行两列 中第二列
plt.subplot(1,2,2)
# plt.title(u"测试2") #注意：在前面加一个u
# 设置标题
plt.title(r'$f(x)=sin(\omega x), \omega = \frac{3}{8} \pi$') 
# 生成图像函数
plt.plot(x1, y1)
# 打印图像
plt.show()