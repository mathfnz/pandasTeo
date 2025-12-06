# %%
import pandas as pd

dfTransacoes = pd.read_csv("../data/transacoes.csv")
dfTransacoes.head()

# %%
dfTransacoes.shape

# %%
dfNovoTransacoes = dfTransacoes.rename(columns={"DescSistemaOrigem":"SistemaOrigem"})
dfNovoTransacoes.head(2)

# %% 
# se quiser usar bastante rename, é mais interessante criar um dicionários

renamed_columns = {"IdTransacao": "idTransacao",
                   "IdCliente":"idCliente"}

dfDicionarioColumns = dfTransacoes.rename(columns=renamed_columns)
print(dfDicionarioColumns.head(2))

# %% 
# se eu usar o implace posso fazer diferentamente
dfDicionarioColumns.rename(columns={"DtCriacao":"dtCriacao"}, inplace=True)
dfDicionarioColumns.head(2)

# %% para chamar mais de 2 colunas
dfDicionarioColumns[["idCliente","QtdePontos"]].head(5)

dfDicionarioColumns = dfDicionarioColumns[["idCliente","QtdePontos","idTransacao"]].head(2)

# %%
