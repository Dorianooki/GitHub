import numpy as np

# 生成10的9次方個隨機點
num_points = 10**9
points = np.random.rand(num_points, 2)

# 計算點到原點的距離
distances = np.sqrt(points[:,0]**2 + points[:,1]**2)

# 計算落在單位圓內的點的數量
points_inside_circle = np.sum(distances <= 1)

# 蒙地卡羅方法計算圓周率
pi_estimate = 4 * points_inside_circle / num_points

print(pi_estimate)