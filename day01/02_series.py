# %%
import pandas as pd

idades = [30, 20, 12, 33, 45, 88, 23, 34, 12, 21, 45, 67, 56, 38, 55]

# antes armazenava em listas, agora são em séries
series_idades = pd.Series(idades)
series_idades # type: ignore

# %%
# media
media_idades = series_idades.mean()
variancia_idades = series_idades.var()
summary_idades = series_idades.describe()
print(f' media: {media_idades}')
print(f' varianca: {variancia_idades}')
print(f'informacoes: {summary_idades}')