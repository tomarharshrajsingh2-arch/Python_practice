import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm

mean_h,std_h = 165,7

prob = 1-norm.cdf(175,mean_h,std_h)

print(f"p(height> 175 cm ) = {prob:.4f}= {prob*100:.1f}")

print(f"68% of people : {mean_h-std_h:.0f}cm to {mean_h+std_h:.0f}cm")
print(f"95% of people: { mean_h-2*std_h:.0f}cm to {mean_h+2 * std_h:.0f}cm")
print(f"99.7% of people: {mean_h-3*std_h:.0f}cm to {mean_h + 3 *std_h:.0f}cm")
