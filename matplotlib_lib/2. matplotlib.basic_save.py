import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,4.5,0.5)
print(x)

plt.figure(figsize=(5,3),dpi=100)
plt.plot(x[:6],x[:6]**2, 'r', label='x^2')
plt.plot(x[5:],x[5:]**2, 'r--')

plt.title('zibi', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('zibi x')
plt.ylabel('zibi y')

plt.xticks([0,1,2,3,4])
plt.legend()

plt.savefig('zibi.png',dpi=300)

plt.show()