
import numpy as np
from scipy import stats
# objective function
def f1(x):
	# return x[0] + x[1]+5
	# return -sum(x)
    f1=0
    for i in range(3):
        f1+=(x[i]**2)
    return f1 
# -------------------------------------
def f2(x):
    f2=(100*(x[0]**2-x[1]**2)+(1-x[1])**2)
    return f2
# -------------------------------------------
def f3(x):
    # if -5.12<=x1<=5.12 &-5.12<=x2<=5.12 &-5.12<=x3<=5.12:
    f3=0
    for i in range(5):
        f3+=(int(x[i]))
    return f3
# -----------------------------------------------
def f4(x):
        f4=0
        for i in range(30):
             f4+=(i*x[i]**4)
        f4+= np.random.normal(0, 1) 
        return f4
# ----------------------------------------------------
def f5(x):
        a0=[-32,-16,0,16,32]*5
        a1=[-32]*5+[-16]*5+[0]*5+[16]*5+[32]*5
        a=[a0,a1]
        for j in range(25):
            for i in range(2):
                  f5_temp=(x[i]-a[i][j])**6
            f5_temp=(j+f5_temp)**-1
        f5=f5_temp+0.002
        return f5
             
             
             


