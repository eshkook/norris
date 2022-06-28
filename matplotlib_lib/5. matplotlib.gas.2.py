import matplotlib.pyplot as plt
import pandas as pd

# why error?? 0:40-0:50 in video

gas=pd.read_csv('gas_prices.csv.txt')

for country in gas:
    if country != 'Year':
        plt.plot(gas.Year,country,marker='.')

plt.xticks(gas.Year[::3])

plt.legend()

plt.show()