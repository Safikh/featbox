from collections import defaultdict

import numpy as np
import pandas as pd

def target_categorizer(feature, target, cuts):
    cut_boundaries = [np.quantile(target, point) for point in np.linspace(0, 1, cuts + 1)]
    boundaries = np.histogram(target, bins=cut_boundaries)[1]
    
    df = pd.DataFrame({"feature": feature, "target": target})
    grouped_feature_dict = df.groupby(by="feature").mean()["target"].to_dict()
    
    centre_index = np.median(range(len(boundaries)))
    category_by_label = defaultdict(lambda: centre_index)
    for key, value in grouped_feature_dict.items():
        for index, boundary in enumerate(boundaries):
            if value <= boundary:
                category_by_label[key] = index
                break
    return df['feature'].map(category_by_label)
    breakpoint()
    