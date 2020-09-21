Initial

# Dataset

- https://ourworldindata.org/coronavirus-source-data
- JSON link https://covid.ourworldindata.org/data/owid-covid-data.json

# Todos





- add app to https://www.data.gv.at/
- check lincense of https://ourworldindata.org/coronavirus-source-data and add to repo
- make joblib model smaller
-


# ToAdd


Register the new environment in ipython
```sh
ipython kernel install --name ml_api_covid --user
```

```sh
touch .git/hooks/pre-commit
code  .git/hooks/pre-commit

#!/bin/sh
# For every ipynb file in the git index, add a Python representation
jupytext --from ipynb --to py:light --pre-commit
```
-