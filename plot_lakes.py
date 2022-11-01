# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-05-11
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Work with data collected
# ----------------------------------------------------------------------------

import os
import sys
import geopandas as gpd
import pandas as pd

thickness = r"C:\Users\ReSEC2021\Downloads\Ice_Thickness_Yellowknife_Nov-Dec.csv"

thick = pd.read_csv(thickness)