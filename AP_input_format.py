import numpy as np
import pandas as pd
import os

for file in os.listdir('./result-csv'):
    new_csv = []
    with open(f'./result-csv/{file}') as f:
        for index, line in enumerate(f.readlines()):
            if index == 0:
                continue
            line = line.strip()
            tmp = line.split(' ')
            for idx in [2, 3, 4, 5]:
                tmp[idx] = str(round(float(tmp[idx])))
            new_csv.append(' '.join(tmp))
    new_csv = pd.DataFrame(np.array(new_csv))
    filename = file.split(".")[0]
    new_csv.to_csv(f'./result-tmp/{filename}.txt', header=False, index=False)