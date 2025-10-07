
# analisis_solar.py
"""
Proyecto: Análisis de producción de energía solar
Autor: Rigoberto Moreno
Descripción:
    Este script carga datos de una planta solar desde un archivo CSV,
    realiza análisis estadístico de la energía diaria y genera gráficos
    guardando los resultados automáticamente.
"""


#-----------------------------------
#Librerías
#-----------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import os

#-------------------------  ----------
#configuración de la rutas
#-----------------------------------
ruta_excel = r"C:\Users\HP OMEN\Desktop\CURSO PYTHON\solar_monitor\data\produccion_solar.xlsx"
ruta_plots= r"C:\Users\HP OMEN\Desktop\CURSO PYTHON\solar_monitor\plots"

#-----------------------------------
#lectura del excel
#-----------------------------------
datos = pd.read_excel(ruta_excel)

# verificar que la primera columna de fecha sea datetime 
datos['Fecha'] = pd.to_datetime(datos['Fecha'])

#-----------------------------------
#Analisis de Energía
#-----------------------------------
energia_total = datos["Energía (kWh)"].sum()
energia_promedio = datos["Energía (kWh)"].mean()
dia_maximo = datos.loc[datos["Energía (kWh)"].idxmax(), "Fecha"].strftime('%d/%m/%Y')

#-----------------------------------
#Resultados de consola
#-----------------------------------
print("Vista previa de los datos:")
print(datos.head())
print(" Resultado del análisis:")
print("Energía total generada:",energia_total,"kWh")
print("Energía Promedio diaria:",round(energia_promedio,2),"kWh")
print("Día de mayor producción:",dia_maximo)

#-----------------------------------
#Gráficos de energía
#-----------------------------------

plt.figure(figsize=(10,5))
plt.plot(datos['Fecha'],datos['Energía (kWh)'], marker='o', linestyle='-', color='orange')
plt.title("Producción diaria de energía")
plt.xlabel("Fecha")
plt.ylabel("Energía (kWh)")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

#Guardar grafico antes de mostrar

ruta_grafico = os.path.join(ruta_plots, "energia_diaria.png")
plt.savefig(ruta_grafico)
plt.show()
print("Gráfico guardado en:", ruta_grafico)