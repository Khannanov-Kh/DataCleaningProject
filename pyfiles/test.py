from trigonometry import sin
import math

pi = math.pi
print('pi:', pi)
for alpha in [0, pi, pi/2, pi/3, pi/4, pi/6]:
    print(f'For angle: {0 if alpha == 0 else "pi/"+str(int(pi/alpha))}, Sine  is ~ {sin(alpha)}')
    
# dfsdf

def find_outliers_quantile(data, feature, left=0.01, right=0.99):
    x = data[feature]
    lower_bound = x.quantile(left)
    upper_bound = x.quantile(right)
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned
