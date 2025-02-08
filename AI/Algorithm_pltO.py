import matplotlib.pyplot as plt
import numpy as np

# 生成输入规模 n 的范围
n = np.linspace(1, 10, 100)

# 计算不同时间复杂度的函数值
constant = np.ones_like(n)
logarithmic = np.log2(n)
linear = n
linear_logarithmic = n * np.log2(n)
quadratic = n**2
exponential = 2**n

# 绘制曲线
plt.figure(figsize=(10, 6))
plt.plot(n, constant, label='O(1)')
plt.plot(n, logarithmic, label='O(log n)')
plt.plot(n, linear, label='O(n)')
plt.plot(n, linear_logarithmic, label='O(n log n)')
plt.plot(n, quadratic, label='O(n^2)')
plt.plot(n, exponential, label='O(2^n)')

# 设置图表标题和坐标轴标签
plt.title('Time Complexity Comparison')
plt.xlabel('Input Size (n)')
plt.ylabel('Time Complexity')

# 添加图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图表
plt.show()