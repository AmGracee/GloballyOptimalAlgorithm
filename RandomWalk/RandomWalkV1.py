

import math
import random

N = 100  # 迭代的次数
step = 0.5 # 初始步长
epsilon = 1e-05 #0.00001
variables = 2 # 变量数目
x = [49,49] # 初始点坐标
walk_num = 1 # 初始化随机游走次数
print("迭代次数:",N)
print("初始步长:",step)
print("epsilon:",epsilon)
print("变量数目:",variables)
print("初始点坐标:",x)

# 定义目标函数
def function(x):
    r = math.sqrt((x[0]-50)**2 + (x[1]-50)**2) + math.e
    f = (math.sin(r) / r) + 1
    return  -f

# 开始随机游走


u = [random.uniform(-1,1) for i in range(variables)]  #[0.0880168903588252, -0.7416845803699941]
print(u)
while(step > epsilon):
    k = 1 # 计数器
    while(k < N):
        u = [random.uniform(-1,1) for i in range(variables)] #[0.0880, -0.74168]随机初始化起点
        u1 = [u[i] / math.sqrt(sum([u[i] ** 2 for i in range(variables)])) for i in range(variables)]
        x1 = [x[i] + step * u1[i] for i in range(variables)]
        if (function(x1) < function(x)):
            k = 1
            x = x1
        else:
            k += 1
    step = step / 2
    print("第%d次随机游走完成。"% walk_num )
    walk_num += 1

    # print("随机游走总次数:", walk_num - 1)
print("最终最优点:", x)
print("最终最优值:", function(x))