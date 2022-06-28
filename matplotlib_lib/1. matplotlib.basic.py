# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html

import matplotlib.pyplot as plt

x=[0,1,2,3,4]
y=[0,2,4,6,8]
z=[0,3,6,9,12]

plt.plot(x,y, label='2x', color='green',linewidth=2,marker='.',markersize=10,markeredgecolor='black',linestyle='--')

plt.plot(x,z, 'b^--', label='3x')

plt.title('zibi', fontdict={'fontname': 'Comic Sans MS', 'fontsize': 20})
plt.xlabel('zibi x')
plt.ylabel('zibi y')

plt.xticks([0,1,2,3,4])
plt.yticks([0,2,4,6,8,10])
plt.legend()
plt.show()

