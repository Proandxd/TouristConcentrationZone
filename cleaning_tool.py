# Import libraries
import numpy as np
import pandas as pd
import os
import glob
import re

# Sort path
root = os.getcwd()
path = os.path.join(root, 'data')
all_files = glob.glob(path + "/*.csv")
keep_cols = ["Grid_ID", "Datetime", "C1", "C2", "C3", "C4", "D1", "E8"]

# Main function
def clean_df():
    for path in all_files:
        match = re.search(r'\\(\w+)\.csv$', path)
        x = pd.read_csv(path, usecols=keep_cols)
        x.to_csv(f"{path}_clean.csv", index=False)
        del(f'{path}.csv')
        del(x)
        del(match)

# Apply cleaning tool
clean_df()
