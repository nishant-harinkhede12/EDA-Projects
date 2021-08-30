url = 'https://raw.githubusercontent.com/krishnaik06/Pandas-Profiling-EDA/master/train.csv'

#pip install pandas_profiling
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df=pd.read_csv(url)


### To Create the Simple report quickly
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)


profile.to_widgets()

profile.to_file("E:\output1.html")

abc = profile.to_file("E:\output1.csv")

abc = profile.to_file("E:\Output1.json")


