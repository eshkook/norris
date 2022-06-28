import matplotlib.pyplot as plt

labels=['A','B','C']
values=[1,4,2]

plt.figure(figsize=(6,4))

bars=plt.bar(labels,values)

patterns=['/','*','O']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.show()