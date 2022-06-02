# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

url = 'Casos_positivos_de_COVID-19_en_Colombia.csv'
data = pd.read_csv(url)

# Conocer las dimensiones del archivo
data.shape

# Conocer las columnas del arhivo
data.columns

# Cantidad de elementos del arhivo
data.size

# Para saber cuantos registros hay por columna

data.count()

# Acceder a los elementos de una columna
data['Código ISO del país']

# Eliminar columnas de un dataset

data.drop('Código ISO del país', axis = 1, inplace=True)
data.drop('Nombre del país', axis = 1, inplace=True)
data.drop('Pertenencia étnica', axis = 1, inplace=True)
data.drop('Nombre del grupo étnico', axis = 1, inplace=True)
data.drop('Fecha de inicio de síntomas', axis = 1, inplace=True)
data.drop('Unidad de medida de edad', axis = 1, inplace=True)
data.drop('Código DIVIPOLA departamento', axis = 1, inplace=True)
data.drop('Código DIVIPOLA municipio', axis = 1, inplace=True)
data.drop('ID de caso', axis = 1, inplace=True)


# Agrupar por columnas los resultados
data['Estado'].value_counts()

# Normalizar la columna de Estado

data.loc[data['Estado'] == 'leve'] = 'Leve'
data.loc[data['Estado'] == 'LEVE'] = 'Leve'

# Cuantas personas murieron por covid en Colombia
cantidad_muertes = data[data['Estado'] == 'Fallecido'].shape[0]
print(cantidad_muertes)

# Normalizar columna sexo
data.loc[data['Sexo'] == 'm'] = 'M'
data.loc[data['Sexo'] == 'f'] = 'F'

# Cuantas mujeres fallecieron en Colombia
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F') ]
cantidad_muertes_mujeres = aux.shape[0]

# Cuantas personas fallecieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Nombre municipio'] == 'BARRANQUILLA') ]
cantidad_muertes_BQ = aux.shape[0]

# Cuantas mujeres fallecieron en Barranquilla
aux = data.loc[(data['Estado'] == 'Fallecido') & (data['Sexo'] == 'F') & (data['Nombre municipio'] == 'BARRANQUILLA') ]
cantidad_muertes_mj_BQ = aux.shape[0]


# Tasa de mortalidad del covid en Colombia

cantidad_casos = data.shape[0]
tasa_mortalidad = cantidad_muertes / cantidad_casos * 100

# Agrupar por Coluna Sexo, Estado
data.groupby(['Sexo', 'Estado']).size()
data.groupby(['Estado', 'Sexo']).size()

# Normalizar columna Estado

data.loc[data['Estado'] == 'M'] = 'Moderado'
data.loc[data['Sexo'] == 'F'] = 'Fallecido'


# Liste por orden descendente las 10 ciudades con mas casos reportados

data['Nombre municipio' ].value_counts().head(10)

# Eliminar filas por condicion

# Curva de contagios en Barranquilila

data[(data['Nombre municipio'] == 'BOGOTA') & (data['Estado'] == 'Fallecido')].groupby('Fecha de diagnóstico').size().plot()

#--------------------------------------------------------------------------------

# Número de casos de contagios en el país
numero_casos = data.shape[0]

# Número de Municipios Afectados
numero_municioios_afectados = len(data['Nombre municipio'].value_counts())

#Liste los municipios afectados (sin repetirlos)
lista_municipios_afectados = set(data['Nombre municipio'])

#Número de personas que se encuentran en atención en casa
personas_atencion_casa = len(data.loc[data['Ubicación del caso'] == 'Casa'])

#Número de personas que se encuentran recuperados
numero_recuperados = len(data.loc[data['Recuperado'] == 'Recuperado'])

#Número de personas que ha fallecido
numero_fallecidos = len(data.loc[data['Recuperado'] == 'Fallecido'])

#Ordenar de Mayor a menor por tipo de caso (Importado, en estudio,
#Relacionado)

#Número de departamentos afectados
numero_deptos_afectados = len(data['Nombre departamento'].value_counts())

#Liste los departamentos afectados(sin repetirlos)
depatamentos_afectados = set(data['Nombre departamento'])

#Ordene de mayor a menor por tipo de atención

#Liste de mayor a menor los 10 departamentos con mas casos de
#contagiados
departamentos_mas_contagiados = data['Nombre departamento'].value_counts().head(10)

#Liste de mayor a menor los 10 departamentos con mas casos de
#fallecidos
fallecidos = data.loc[data['Recuperado'] == 'Fallecido']
departamentos_con_mas_fallecidos = fallecidos['Nombre departamento'].value_counts().head(10)

#Liste de mayor a menor los 10 departamentos con mas casos de
#recuperados
recuperados = data.loc[data['Recuperado'] == 'Recuperado']
departamentos_con_mas_recuperados = recuperados['Nombre departamento'].value_counts().head(10)

#Liste de mayor a menor los 10 municipios con mas casos de
#contagiados
municipios_con_mas_contagios = data['Nombre de municipio'].value_counts().head(10)

#Liste de mayor a menor los 10 municipios con mas casos de
#fallecidos
fallecidos = data.loc[data['Recuperado'] == 'Fallecido']
municipios_con_mas_fallecidos = fallecidos['Nombre municipio'].value_counts().head(10)
