import matplotlib.pyplot as plt
import numpy as np
g = input("bez spacji , jak jest jeden x to 1x nie x: ")
y = list(g)
z = y.index("^")
print(z)
q = []
f = []
r = []
for i in range(0, z-1):
    q.append(y[i])
a = float("".join(q))
d = y.index("x", z+2)
for o in range(y.index(y[z+2]), d):
    f.append(y[o])
b = float("".join(f))
print(b)
for u in range(d+1, len(y)):
    r.append(y[u])
c = float("".join(r))
print(c)
delta = (b**2)- (4*a*c)
print(delta)
if delta > 0:
    xone =  ((-b) + (delta**0.5)) / (2*a)
    xtwo =  ((-b) - (delta**0.5)) / (2*a)
elif delta == 0:
    xone =  (-b) / (2*a)
    xtwo =  "brak"
elif delta < 0:
    xone = "brak"
    xtwo = "brak"
print(f"x1 = {xone}, x2 = {xtwo}")
p = np.linspace(-20, 20, 800)
j = a*p**2+b*p+c
plt.plot(p, j)
plt.show()
