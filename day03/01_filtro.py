# %%
import pandas as pd

dfTransacoes = pd.read_csv("../data/transacoes.csv")
dfTransacoes.head(2)

# %% transacoes > 50 pontos
filtro = (dfTransacoes["QtdePontos"] > 50) & (dfTransacoes["QtdePontos"] < 500)
dfTransacoes[filtro].head(2)