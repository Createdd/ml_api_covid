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
import numpy as np

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
import jupyternotify
ip = get_ipython()
ip.register_magics(jupyternotify.JupyterNotifyMagics)
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
from sklearn.model_selection import train_test_split

# ## Encode categorical

nominal = df.select_dtypes(include=['object']).copy()
nominal_cols = nominal.columns.tolist()
nominal_cols

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

# ## Split into train and test set

X = df.drop(columns=['new_cases'])
y = df.new_cases
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

X_train

# # Add ML

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score 
from sklearn.model_selection import RandomizedSearchCV
from joblib import dump, load

rf = RandomForestRegressor(
    n_estimators = 100, # 400 
    random_state = 0, 
    max_depth=30)

rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)

print(f'{r2_score(y_test, y_pred):.2%}')

# ## Improve hyperparameters
#
# Best params for n_estimators and max_depth are
#
# `{'n_estimators': 400, 'max_depth': 30}`

random_grid = {'n_estimators': np.arange(200,600,100),
#                'max_features': ['auto', 'sqrt'],
               'max_depth': np.arange(10,40,10)}
#                'min_samples_split': [2, 5],
#                'min_samples_leaf': [2,4]}#,
#                'bootstrap': [True, False]}

rf_random = RandomizedSearchCV(
    estimator = rf, 
    param_distributions = random_grid, 
    n_iter = 100, cv = 3, verbose=2, random_state=0)

# +
# rf_random.fit(X_train, y_train)

# +
# rf_random.best_params_
# -

# ## Re-run 

# +
# rf = RandomForestRegressor(**rf_random.best_params_, random_state = 1)

# +
# y_pred = rf.predict(X_test)

# +
# print(f'{r2_score(y_test, y_pred):.2%}')
# -

# # Save model

# dump(rf, 'rf_model.joblib') 
dump(rf, 'rf_model.joblib',compress=3)
# dump(rf, 'rf_model.pkl.z')

# # Predict on country

input_val = 'Germany'

encoder.fit_transform(df_orig['location'])

encode_ind = (encoder.classes_).tolist().index(input_val)

df_orig[df_orig.location == input_val]

to_pred = X[X.location == encode_ind].iloc[-1].values.reshape(1,-1)

rf.predict(to_pred)[0] 


