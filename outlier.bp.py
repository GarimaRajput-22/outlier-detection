import numpy as np
import matplotlib as plt
dataset = [11,10,12,14,12,15,14,13,
15,102,12,14,17,19,107,10,13,12,14,12,108,12,11,14,13,15,10,15,12,10,14,13,15,10]
dataset = sorted(dataset)
print (type(dataset))
print(dataset)
q1 = np.percentile (dataset,[25])
print(q1)
q3 = np.percentile (dataset,[75])
print(q3)
iqr = q3-q1
print(iqr)
lower_fence = q1-(1.5*iqr)
higher_fence = q3+(1.5*iqr)
print (lower_fence)
print (higher_fence)
outliers = [x for x in dataset
    if x<lower_fence or x > higher_fence]
print(outliers)
import matplotlib.pyplot as plt
import seaborn as sns 
boxplot=sns.boxplot(data=dataset)
plt.show()


    