# %%
import pandas as pd

#leio o arquivo
df = pd.read_csv("../data/clientes.csv")
print(df)

# %%
#salvo o arquivo
df.to_csv("clientes.csv", index=False, sep=",")
print(df)

# %%
df.to_parquet("clientes.parquet", index=False)
df_parquet = pd.read_parquet("clientes.parquet")
print(df_parquet)
