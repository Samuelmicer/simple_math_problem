import random
def check_if_in_half_circle(a,b,c,d):
    '''
    A,B,C,D为圆内任意4个点,四个点与圆心、x轴形成的夹角分别为a,b,c,d。
    判断四个点是否在同一个半圆内。
    ''' 
    angle_list = [a,b,c,d]
    sorted_angle_list = sorted(angle_list)
    if sorted_angle_list[3] - sorted_angle_list[0] <= 180:
        return True
    
    for _ in range(3):
        sorted_angle_list[-1] -= 360
        sorted_angle_list = sorted(sorted_angle_list)
        if sorted_angle_list[3] - sorted_angle_list[0] <= 180:
            return True
    
    return False
    

sim_num = 10000000
count = 0
for i in range(sim_num):
    a = random.uniform(0,360)
    b = random.uniform(0,360)
    c = random.uniform(0,360)
    d = random.uniform(0,360)
    if check_if_in_half_circle(a,b,c,d):
        count += 1

print(f'模拟次数:{sim_num}, 四点在同一半圆内的次数:{count}, 概率:{count/sim_num}')
    