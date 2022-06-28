import matplotlib.pyplot as plt
import pandas as pd

fifa=pd.read_csv('fifa_data.csv.txt')

# get rid of the lbs:
fifa.Weight=[int(x.strip('lbs')) if type(x)==str else x for x in fifa.Weight]
print(fifa.Weight)

# automatic style :
plt.style.use('ggplot')

light=fifa.loc[fifa.Weight<125].count()[0]
medium=fifa.loc[(fifa.Weight>=125) & (fifa.Weight<200)].count()[0]
heavy=fifa.loc[fifa.Weight>200].count()[0]

weights=[light,medium,heavy]
Labels=['Under 125','125-200', 'Over 200']
Explode=(.4,0,.3)

plt.pie(weights,labels=Labels,autopct='%.2f %%',pctdistance=0.8,explode=Explode)
plt.title('weight distribution')

plt.show()