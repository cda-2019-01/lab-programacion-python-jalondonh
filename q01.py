##
## Imprima la suma de la segunda columna.
##
import pandas as pd
import numpy as np
df = pd.read_csv("data.csv", sep="\t+|\s+",engine='python',header=None)
q01 = df[1].sum()
print(q01)