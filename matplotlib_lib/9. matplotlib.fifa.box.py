import matplotlib.pyplot as plt
import pandas as pd

fifa=pd.read_csv('fifa_data.csv.txt')

plt.style.use('default')
plt.figure(figsize=(5,8))

barcelona=fifa.loc[fifa.Club=='FC Barcelona']['Overall']
madrid=fifa.loc[fifa.Club=='Real Madrid']['Overall']

Labels=['FC Barcelona','Real Madrid']

# the patch_artist is for the next comment 'ppp' below to work
boxes=plt.boxplot([barcelona,madrid],labels=Labels,patch_artist=True)

for box in boxes['boxes']:
    # set edge color:
    box.set(color='#4286f4',linewidth=2)
    # ppp: change fill color:
    box.set(facecolor='#e0e0e0')

plt.title('team comparison')
plt.ylabel('fifa overall rating')

plt.show()

