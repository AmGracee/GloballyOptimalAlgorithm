import math
import random

N = 100  # 迭代的次数
step = 10 # 初始步长  步长的设置影响很大，比如设置0.5
epsilon = 1e-05 #0.00001
variables = 2 # 变量数目
x = [-100,-10] # 初始点坐标
walk_num = 1 # 初始化随机游走次数
n = 10  # 每次随机生成向量u的数目

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
        x1_list = [] #存放x标准化后的值，然后取最小
        for i in range(n):

            u = [random.uniform(-1,1) for i1 in range(variables)] #[0.0880, -0.74168]随机初始化起点
            u1 = [u[i3] / math.sqrt(sum([u[i2] ** 2 for i2 in range(variables)])) for i3 in range(variables)]
            x1 = [x[i4] + step * u1[i4] for i4 in range(variables)]
            x1_list.append(x1)
        f1_list = [function(x1) for x1 in x1_list]
        f1_min = min(f1_list)
        f1_index = f1_list.index(f1_min) # 取最小值的索引
        x1_min = x1_list[f1_index]#取最小值f1_min对应的x1
        if (f1_min < function(x)):
            k = 1
            x = x1_min
        else:
            k += 1
    step = step / 2
    print("第%d次随机游走完成。"% walk_num )
    walk_num += 1

    # print("随机游走总次数:", walk_num - 1)
print("最终最优点:", x)
print("最终最优值:", function(x))