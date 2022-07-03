import numpy as np
import pandas as pd

from target_categorizer import target_categorizer

df = pd.read_csv('test_data/cardata.csv')
# print(df.head())
breakpoint()
target_categorizer(df['Make'], df['MSRP'], cuts=4)
