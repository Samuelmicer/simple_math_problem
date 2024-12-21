# 脑筋急转弯x

## 问题1

![img1](problem1/question.png)

### 蒙特卡洛模拟

[MonteCarlo.py](problem1/MonteCarlo.py)

思路是将四个点的角度大小进行排序，当最大的角度减去最小的角度小于180度时，四个点必定在同一个半圆上。

但是可能存在特殊情况，当四个点所在的半圆横跨x轴正半轴时，需要将最大的角度-360度，再次进行上述判断。最多有可能有三个跨过了x轴正半轴，因此需要循环三次。

![p1/p1](problem1/p1.png)

### 理论推导

![theory](problem1/p2.jpg)