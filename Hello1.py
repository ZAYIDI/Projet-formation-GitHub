# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 15:24:12 2024

@author: ZAYID
"""

print("Hello word 1!")




print("Hello word 2!")



import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-2, 2, 100)

y = np.sinc(2*x)


plt.plot(x, y, 'b:*')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sinus cardinal")
plt.grid()
plt.show()