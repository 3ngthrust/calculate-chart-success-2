#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 3ngthrust
"""

import matplotlib.pyplot as plt

x = list(range(1995,2018,1))
song_values = [184, 136, 5328, 4714, 7065, 8509, 1329, 49, 0, 79, 6414, 722, 0, 4850, 5814, 12625, 17171, 13925, 10151, 19374, 22272, 16905, 4633]

fig = plt.figure(1)
plt.plot(x, song_values, marker='o', label="Max Martin") 

plt.title('Chart Success of Max Martin')
plt.xlabel('Year')
plt.ylabel('Chart Success (Accumulated Song Values)')
#plt.legend(loc='upper left')

fig.savefig('Max_Martin_Chart_Success.png', dpi = 300)

plt.show()
