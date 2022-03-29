# %% [markdown]
# # Importando bibliotecas

# %%
import pandas as pd

# %% [markdown]
# # Codigos loucos

# %%
df_titanic = pd.read_csv('data/tested.csv')
df_titanic

# %%
df_titanic.head()

# %%
df_titanic.tail()

# %%
df_titanic.info()

# %%
type(df_titanic)

# %%
idade = df_titanic['Age']
idade

# %%
type(idade)

# %%
df_titanic[['Age']]

# %%
df_titanic.columns

# %%
df_titanic.rename(columns={'PassengerId':'IdPassageiro', 'Survived':'Sobrevivel', 'Pclass':'Classe', 'Name':'Nome', 'Sex':'Sexo', 'Age':'Idade', 'SibSp':'n_familia',
       'Parch':'n_parentes', 'Ticket':'num_Bilhete', 'Fare':'preço_bilhete', 'Cabin':'num_cabine', 'Embarked':'origem_embarque'}, inplace=True)

# %%
df_titanic

# %%
idade

# %%
df_titanic['Sexo'].value_counts()

# %%
df_titanic.describe()

# %%
df_titanic.drop(columns=['num_cabine','num_Bilhete'], inplace=True)

# %%
df_titanic


