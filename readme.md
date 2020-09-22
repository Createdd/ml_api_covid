Initial

# Dataset

- https://ourworldindata.org/coronavirus-source-data
- JSON link https://covid.ourworldindata.org/data/owid-covid-data.json

# Todos





- add app to https://www.data.gv.at/
- check license of https://ourworldindata.org/coronavirus-source-data and add to repo
- make joblib model smaller https://stackoverflow.com/questions/43591621/trained-machine-learning-model-is-too-big
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

chmod +x .git/hooks/pre-commit
```



docker:

```sh
docker build -t ml_api_covid .
```

```sh
docker run -d -p 80:8080 ml_api_covid
```

zappa:

```sh
zappa init
```

```sh
zappa deploy dev
```


# Reading

- https://www.bluematador.com/blog/serverless-in-aws-lambda-vs-fargate aws lambda vs fargate
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html billing alarm
- https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507




zappa issue with pandas https://github.com/Miserlou/Zappa/issues/1927


do not enter name for s3 bucket as it cannot be found