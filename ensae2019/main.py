import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs
import cartopy.feature as cfeature

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
        raise ValueError
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

def plot_gif_geo_time_value(x, y,fig,ax,year, value, name='', hue='', **kwargs): 
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
    def animate(i):
        ax.clear()
        #ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
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
        
    
    animation = anim.FuncAnimation(fig, animate, frames=len(year), blit=False, repeat=True)

    animation.save("output.gif", fps=1)
