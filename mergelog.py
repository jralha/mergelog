#%% Libraries
import lasio 
import glob
import matplotlib.pyplot as plt
import numpy as np
from tqdm.auto import tqdm
import pandas as pd

#%% Load data
folder = '\\\\strgpetrec\\Projetos e Servicos\\Petrofisica\\Petrofisica de Poco\\DADOS_TODOS_POCOS\\BACIA DE SANTOS\\2-ANP-2A-RJS\\LAS'


#%% List with all las files as DFs
dfs=[]
for file in tqdm(glob.glob(folder + "/*.las")):
    las = lasio.read(file)
    df = las.df()
    dfs.append(df)

#%% Curves
li=[]
for df in dfs:
    li.append(list(df.columns))
curves = np.unique([y for x in li for y in x])

#%%
temp_curve=[]
merged_curves=[]
for curve in tqdm(curves):
    for df in dfs:
        try:
            tmp_series = df[curve]
            tmp_series.iloc[50:-50]
            temp_curve.append(tmp_series)
        except:
            continue
        
    merged = pd.concat(temp_curve).sort_index().groupby('DEPT').min()
    merged.name = curve
    merged_curves.append(merged)

full_df = pd.DataFrame(merged_curves).T

# %%
full_df.to_excel('test.xlsx')

# %%
