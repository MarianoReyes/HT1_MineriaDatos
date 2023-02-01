import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from quickda.clean_data import *

datos = pd.read_csv("baseball_reference_2016_scrape.csv")

# 1.1
# print(datos.head())

# print(datos.dtypes)

# 1.2
# Realizada en documento

# 1.3
# plt.hist(datos['home_team_runs'])
# plt.xlabel('Carreras de equipo local')
# plt.ylabel('Frecuencia')
# plt.title('Histograma para las carreras de equipo local')
# plt.show()

# plt.scatter(datos['home_team_runs'], datos['away_team_runs'])
# plt.xlabel('Carreras de equipo local')
# plt.ylabel('Carreras de equipo visitante')
# plt.title('Gráfico de dispersión para carreras de equipo local vs. carreras de equipo visitante')
# plt.show()

# sns.boxplot(datos['home_team_runs'])
# plt.xlabel('Carreras de equipo local')
# plt.title('Gráfico de caja para las carreras de equipo local')
# plt.show()

# sns.histplot(datos['away_team_errors'])
# plt.xlabel('Errores de equipo visitante')
# plt.ylabel('Frecuencia')
# plt.title('Histograma para los errores de equipo visitante')
# plt.show()

# sns.kdeplot(datos['away_team_hits'].dropna())
# plt.xlabel('Hits de equipo visitante')
# plt.ylabel('Densidad')
# plt.title('Gráfico de densidad para los hits de equipo visitante')
# plt.show()

# 1.4
# Seleccione solo las variables numéricas
# numeric_vars = datos.select_dtypes(include=[np.number])
# Calcular la matriz de correlación
# corr = numeric_vars.corr()
# Gráfico de calor de la matriz de correlación
# sns.heatmap(corr, annot=True, cmap='coolwarm')
# plt.show()

# 1.5
# var = 'away_team'
# table = datos[var].value_counts(normalize=True)
# Gráfico de proporción
# table.plot(kind='pie', autopct='%1.1f%%')
# plt.axis('equal')
# plt.title("Proporción de '{}'".format(var))
# plt.show()

# var = 'game_type'
# table = datos[var].value_counts()
# Gráfico de barras
# table.plot(kind='bar')
# plt.title("Frecuencia de '{}'".format(var))
# plt.ylabel("Frecuencia")
# plt.show()

# var = 'home_team'
# table = datos[var].value_counts()
# Gráfico de barras
# table.plot(kind='bar')
# plt.title("Frecuencia de '{}'".format(var))
# plt.xlabel(var)
# plt.ylabel("Frecuencia")
# plt.show()


# 1.6

datos = clean(datos, method="standardize")
datos = clean(datos, method="duplicates")
datos = clean(datos, method="replaceval",
              # Si no se dan columnas, lo hace en todas
              columns=['attendance'],
              to_replace="]",  # Si no se da el valor que debe ser reemplazado, no cambia nada
              value=" ")   # Si no se da el valor con que se reemplazará, utiliza el valor nulo
datos.to_csv("clean_files.csv", index=False)