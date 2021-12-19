import numpy as np
from scipy import stats as st


speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
y=st.mode(speed)
print(np.mean(speed))
print(np.median(speed))
print(y[0],type(y[0]))