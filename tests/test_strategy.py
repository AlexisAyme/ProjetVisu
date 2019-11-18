import pandas as pd 
df_metro = pd.read_csv("data/data_polution.csv")
lim_metropole = [-5, 10, 41, 52]
#from ensae2019 import plot_geo_time_value # nos fonctions 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import unittest
##
fig, axs = plt.subplots(2, 2, figsize=(20,20), subplot_kw={'projection': ccrs.PlateCarree()})

x, y = df_metro['LLX'], df_metro['LLY']
years = range(2004, 2008)
years_str = [str(year) for year in years]
values = df_metro[[colname for colname in df_metro.columns.values if colname[-4:] in years_str]].astype('float')
##


    

class test_algo(unittest.TestCase):

    def test_years(self):
        with self.assertRaises(ValueError):
            plot_geo_time_value(x, y, year=2, value=values, proj='mercator', axs=axs)

if __name__ == '__main__':
    unittest.main()
