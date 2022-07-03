import numpy as np
import pandas as pd

from featbox.target_categorizer import target_categorizer

from tests import DATADIR

def test_tc_1():
    df = pd.read_csv(DATADIR + '/cardata.csv')
    assert target_categorizer(df['Make'], df['MSRP'], cuts=4).nunique() == 4
