import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd

lim_metropole = [-5, 10, 41, 52]

def plot_geo_time_value(x, y, year, value,  axs=None, name='', hue='', **kwargs):
    """
    Visualise l'évolution temporelle d'une donnée numérique
    géolocalisée.

    :param x: longitudes (vecteur)
    :param y: latitudes (vecteur)
    :param year: années (vecteur)
    :param value: valeurs numériques à représenter (DataFrame ou numpy array de taille n_observations * n_years)
    :param axs: axes matplotlib sur lesquels tracer (vecteur ou numpay array)
    :param name: noms des lieux  (vecteur)
    :param hue: sens de la valeur numérique (:math:`CO_2`, Ammoniac, ...)
    :param kwargs: paramètres additionnels
    """
    if type(year) is not range:
        raise NameError("Invalid type for years argument")
    elif type(x) is not pandas.core.series.Series:
        raise NameError("Invalid type for x argument")
    elif type(y) is not pandas.core.series.Series:
        raise NameError("Invalid type for y argument")
    elif type(values) is not pandas.core.frame.DataFrame:
        raise NameError("Invalid type for values argument")
    i=0
    for ax1 in axs :
        for ax in ax1 :
            ax.set_extent(lim_metropole)
            ax.add_feature(cfeature.OCEAN.with_scale('50m'))
            ax.add_feature(cfeature.COASTLINE.with_scale('50m'))
            ax.add_feature(cfeature.RIVERS.with_scale('50m'))
            ax.add_feature(cfeature.BORDERS.with_scale('50m'), linestyle=':')
            ax.scatter(x, y, s=value.iloc[:,i] ** 0.5 / 5, alpha=0.5)
            if hue!= '':
                ax.set_title(name+ " " + str(year[i])+": Quantité de "+ str(hue))
            else:
                ax.set_title(name+ " " + str(year[i]))
            i=i+1
    plt.savefig("figure.pdf")
     
