# %%
import pandas as pd

dfClientes = pd.read_csv("../data/clientes.csv")
print(dfClientes)

# %% - 5 primeiras linhas
dfClientes.head()

# %% - 5 últimas linhas
dfClientes.tail()

# %%
dfClientes.shape # (linhas, colunas)

# %%
dfClientes.columns # nome das colunas

# %%
dfClientes.index

# %%
dfClientes.info()