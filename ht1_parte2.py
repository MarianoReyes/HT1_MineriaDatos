import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt




data = pd.read_csv("new_file.csv")


data = data[data["attendance"].str.isdigit()]

#se eliminaron las columnas que no se necesitan
del data["date"]
del data["field_type"]
del data["boxscore_url"]
del data["start_time"]




v = data["game_duration"].str.split(":", expand=True).astype(int)
data["game_duration"] = v[0]*60 +v[1]

data = data.astype({"attendance": int}, {"game_duration": int})

#se codifican las variables
def codif_y_ligar(dataframe_original, varcodeadas):
    dummies = pd.get_dummies(dataframe_original[[varcodeadas]])
    res = pd.concat([dataframe_original, dummies], axis = 1)
    res = res.drop([varcodeadas], axis = 1)
    return(res) 

#se codifican variables para leer
varcodeadas = ["away_team", "game_type", "home_team", "venue"]
for variable in varcodeadas:
    data = codif_y_ligar(data, variable)

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values


transCol = ColumnTransformer(transformers=[("encoder", OneHotEncoder(), [3])], remainder="passthrough")
X = np.array(transCol.fit_transform(X))
X_entreno, X_prueba, y_entreno, y_prueba = train_test_split(X, y, test_size = 0.2, random_state = 0)

#calculos
regresor = LinearRegression()
regresor.fit(X_entreno, y_entreno)
y_pred = regresor.predict(X_prueba)
np.set_printoptions(precision=2)


#resultados finales
print("Regresion lineal")
print(regresor.coef_)

print("")
print("Prediccion")

print(regresor.predict([[30000]*121])*-1)



r2=1 - (1-regresor.score(X_entreno, y_entreno))*(len(y_entreno)-1)/(len(y_entreno)-X_entreno.shape[1]-1)
print("")
print("R^2")
print(r2)

model = LinearRegression().fit(X_entreno, y_entreno)

# Intercepto y coeficiente
intercept = model.intercept_
coef = model.coef_[0]

# Imprimir la ecuacion
print("")
print("Ejercicio 2.3, constantes del modelo y la ecuación que representan")
print("y = {:.2f} + {:.2f} * x".format(intercept, coef))