import pytest
import numpy as np
import pandas as pd

from featbox.target_categorizer import target_categorizer

def test_tc_1():
    df = pd.read_csv('cardata.csv')
    assert target_categorizer(df['Make'], df['MSRP'], cuts=4).nunique() == 4
