#%%
import pandas as pd

idades = [
    33, 12, 23, 56 , 7, 88, 25, 25, 26, 78, 3, 35, 6
]

nomes = ["Matheus", "Lucas", "fabinho", "Paulinho",
         "Douglas", "Elias", "Chicão", "Felipe", "Ronaldo", "André Santos", "Jadshow",
         "Reidriguinho", "Reinato Augusto"]

grupoTrabalho = ["A", "B", "B", "A",
                     "B", "B", "A", "A",
                     "B", "B", "A", "A", "A"]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)
series_grupoTrabalho = pd.Series(grupoTrabalho)
print(series_idades)
print(series_nomes)

# %%
df = pd.DataFrame()
df["Idades"] = series_idades
df["Nomes"] = series_nomes
df["Grupo de Trabalho"] = series_grupoTrabalho
print(df)
type(df)

# %%
# como acessar um valor em específico
df["Nomes"] # selecionei a coluna da tabela
# %%
# acessar uma linha específico
df.iloc[3] # a terceira linha
# %%
df.iloc[8]["Nomes"] # traz especifico somente o nome
