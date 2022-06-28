import matplotlib.pyplot as plt
import pandas as pd

gas=pd.read_csv('gas_prices.csv.txt')

plt.plot(gas.Year,gas.USA, 'r.-',label='usa')
plt.plot(gas.Year,gas.Canada, 'b.-',label='robbin')
plt.plot(gas['Year'],gas['South Korea'], 'g.-',label='parasite')

plt.xticks(gas.Year[::3].tolist()+[2011])

plt.legend()

plt.show()
