import numpy as np   
import matplotlib.pyplot as plt
%matplotlib inline

incomedata = np.random.normal(200, 1500, 500)

np.mean(incomedata)

plt.hist(incomedata, 50)
plt.show()