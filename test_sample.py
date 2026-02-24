import numpy as np

x = np.array([1, 2, 3, 4])
y = np.tile(x, [4, 1]).reshape(4, 4)

print(y)
print(y.shape)
print(y.size)
print(y.ndim)
import pandas as pd
import numpy as np
s = pd.Series(np.arange(5), index=["a", "b", "c", "d", "e"])
print(s)

s = pd.Series(np.linspace(0, 1, 2))
print(s)
