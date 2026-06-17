import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from scipy import stats

salaries= [22,28,35,42,38,55,48,48,72,85,30,48,52,65,28,34,41,58,75,90]

mean = np.mean(salaries)
median =np.median(salaries)
mode=stats.mode(salaries,keepdims=True).mode[0]

print(f"Mean (Average): Rs.{mean:.1f}K")
print(f"Median (middle values): Rs.{median}K")
print(f"Mode (Most common): Rs.{mode}K")


std=np.std(salaries)
var=np.var(salaries)
rng=max(salaries)-min(salaries)
q1=np.percentile(salaries,25)
q3=np.percentile(salaries,75)
iqr=q3-q1
print(f"std deviation : {std: .2f}")
print(f"IQR: {iqr}k  (q1={q1}), (q3={q3})")

lower = q1 -1.5*iqr
upper = q3 + 1.5*iqr

outliers= [x for x in salaries if x<lower or x>upper]

print(f" Outliers : {outliers}")