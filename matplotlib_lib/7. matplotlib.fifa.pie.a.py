import matplotlib.pyplot as plt
import pandas as pd

fifa=pd.read_csv('fifa_data.csv.txt')

left=fifa.loc[fifa['Preferred Foot']=='Left'].count()[0]
right=fifa.loc[fifa['Preferred Foot']=='Right'].count()[0]
print(left)

Labels=['Left','Right']
Colors=['#aabbcc','#abcdef']

plt.pie([left,right],labels=Labels,colors=Colors,autopct='%.2f %%')
plt.title('foot preference')

plt.show()