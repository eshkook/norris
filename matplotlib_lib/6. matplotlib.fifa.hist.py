import matplotlib.pyplot as plt
import pandas as pd

fifa=pd.read_csv('fifa_data.csv.txt')

Bins=[40,50,60,70,80,90,100]

#use color picker from google
plt.hist(fifa.Overall,bins=Bins,color='#abcdef')
plt.title('players')
plt.xlabel('skill')
plt.ylabel('num of players')

plt.xticks(Bins)

plt.show()