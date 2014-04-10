#!/usr/bin/python
# -*- coding: utf-8 -*-

"""colourValues.py: Stores the upper and lower range values for the colours to be detected."""

import numpy as np

__author__ = 'Noah Ingham'
__email__ = 'noah@ingham.com.au'

upperRange={'white': [60,30,255],   'blue': [140,255,255],  'red': [180,255,255] }
lowerRange={'white': [0,0,100],     'blue': [100,100,100],        'red': [130,100,100] }

rectangleC={'white': [0,0,0],     'blue': [180,127,255],        'red': [0,255,255] }

upperRange = {k: np.array(v) for k, v in upperRange.items()}
lowerRange = {k: np.array(v) for k, v in lowerRange.items()}
