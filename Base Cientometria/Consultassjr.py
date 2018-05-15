import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

data = pd.read_csv('Cientometria\\resultadoConsultaSJR.txt', header=0, names = ["ano","sjrJournalId","areaConhecimento","sjrScoreValue","nomeGrupo","nomeAutor","nomePaper"])
#"ano","sjrJournalId","areaConhecimento","sjrScoreValue","nomeGrupo","nomeAutor","nomePaper"
#"2012","1413-9324","Forestry","0.2530","DEF/I","Afonso Figueiredo Filho","Dinâmica da distribuição diamétrica na arborização de ruas da cidade de Curitiba, Paraná, Brasil"


data = data.drop('sjrJournalId',axis=1)
data = data.drop('nomePaper',axis=1)
#"ano",     "areaConhecimento",     "sjrScoreValue",     "nomeGrupo",    "nomeAutor",
#"2012",    "Forestry",         "0.2530",            "DEF/I",        "Afonso Figueiredo Filho"


def groupSumSort(data, groupBy, sortBy=False, ascending=True):
    df = data.groupby(by=groupBy).sum()
    df = df[:-1]
    if sortBy:
        df = df.sort_values(by=sortBy, ascending=ascending)
    return df

# imprimindo o score geral por ano
input = data.drop(["nomeGrupo", "areaConhecimento", "nomeAutor"], axis=1)
print(input.groupby(['ano']).sum())
df = groupSumSort(input,['ano'])
plt.plot (df['sjrScoreValue'], color = 'green', marker = 'o', linestyle = 'solid')
plt.title ("Score geral por ano")
plt.ylabel("Score")
plt.xlabel("ano")
plt.show()

# imprimindo o score geral por grupo
input = data.drop(["ano", "areaConhecimento"], axis=1)
df = groupSumSort(input, ['nomeGrupo'], ['sjrScoreValue'], False)
print (df)
y_axis = df['sjrScoreValue']
x_axis = df.index.values
width_n = 0.8
bar_color = 'yellow'

plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
plt.xticks(x_axis,x_axis,rotation= 'vertical')
plt.show()


# imprimindo o score geral por area
input = data.drop(["ano","nomeGrupo"], axis=1)
df = groupSumSort(input, ['areaConhecimento'], ['sjrScoreValue'], False)

y_axis = df['sjrScoreValue']
x_axis = df.index.values
width_n = 0.6
bar_color = 'blue'

plt.bar(x_axis, y_axis, width=width_n, color=bar_color)
plt.xticks(x_axis,x_axis,rotation= 'vertical')
plt.show()