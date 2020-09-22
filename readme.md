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

## S3

- https://console.aws.amazon.com/s3/


1. "create bucket"
2. give name and leave rest as default
3. "create bucket"


add policy for interacting with boto3

```sh
{
      "Effect": "Allow",
      "Action": [
        "s3:CreateBucket",
        "s3:ListBucket",
        "s3:ListBucketMultipartUploads",
        "s3:ListAllMyBuckets",
        "s3:GetObject"
      ],
      "Resource": [
        "arn:aws:s3:::zappa-*",
        "arn:aws:s3:::*"
      ]
    }
```


# Reading


- https://towardsdatascience.com/how-to-deploy-a-machine-learning-model-on-aws-lambda-24c36dcaed20


- https://www.bluematador.com/blog/serverless-in-aws-lambda-vs-fargate aws lambda vs fargate
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html billing alarm
- https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507
- https://stackoverflow.com/questions/62941174/how-to-write-load-machine-learning-model-to-from-s3-bucket-through-joblib
-

zappa issue with pandas https://github.com/Miserlou/Zappa/issues/1927

aws s3

- https://stackabuse.com/file-management-with-aws-s3-python-and-flask/


do not enter name for s3 bucket as it cannot be found

# additional

- https://www.freecodecamp.org/news/what-we-learned-by-serving-machine-learning-models-using-aws-lambda-c70b303404a1/