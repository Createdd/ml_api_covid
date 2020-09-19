# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.5.2
#   kernelspec:
#     display_name: ml_api_covid
#     language: python
#     name: ml_api_covid
# ---

# # Import Libs

# +
import os
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
# -

# # Load data

url_to_covid = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'

df_orig = pd.read_csv(url_to_covid)

# # Understand structure

df_orig.location.unique()

df = df_orig[df_orig.location == 'Austria']

df

_ = plt.figure(figsize=(30, 15))
sns.scatterplot(sorted(df.date), df.new_cases);

# ## Check missing

df = df_orig.copy()

df.info()

# +
percent_missing = df.isnull().sum() * 100 / len(df)
missing_value_df = pd.DataFrame({'column_name': df.columns,
                                 'percent_missing': percent_missing})

missing_value_df.sort_values('percent_missing', inplace=True, ascending=False)
missing_value_df
# -

cols_too_many_missing = missing_value_df[missing_value_df.percent_missing > 50].index.tolist()
len(cols_too_many_missing)
cols_too_many_missing

len(df.columns)

df_reduced = df.drop(columns=cols_too_many_missing)

len(df_reduced.columns)

df_reduced

df = df_reduced

df.info()

missing_iso_code = df[df.iso_code.isna()]
df = df.drop(index=missing_iso_code.index)

missing_continent = df[df.continent.isna()]
df = df.drop(index=missing_continent.index)

for col in df.columns: 
    col, df[col].isna().sum()

# Now we have removed the rows and columns that contained too many Nans.

# # Preprocess for ML
#
# Now we need to encode the nominal variables and impute nans of the numerical variables.

from sklearn.preprocessing import LabelEncoder

# ## Encode categorical

nominal = df.select_dtypes(include=['object']).copy()
nominal_cols = nominal.columns.tolist()
nominal_cols

df.tests_units.value_counts(dropna=False)

encoder = LabelEncoder()
for col in nominal_cols:
    col
    if df[col].isna().sum() > 0:
        df[col].fillna('MISSING', inplace=True)
    df[col] = encoder.fit_transform(df[col])

for col in nominal_cols:
    df[col].unique()

# ## Impute missing values of numerical

numerical = df.select_dtypes(include=['float64']).copy()
numerical

df.total_cases

for col in numerical:
    df[col].fillna((df[col].mean()), inplace=True)

df.isna().sum().sum() == 0

# Now the dataset has no Nans and is completely encoded.

# # Add ML




