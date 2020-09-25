<br />
<p align="center">
  <h3 align="center">Predict Covid per country</h3>

  <p align="center">
    Predict new cases of covid-19 infections
    <br />
    <a href="https://github.com/Createdd/Writing/blob/master/2020/articles/pythonApi.md"><strong>Explore the tutorial »</strong></a>
    <br />
    <br />
  </p>
</p>

---

![gif of app functionality](http://g.recordit.co/7JGIL7T9GC.gif)

# About The Project

This is the API Code for my tutorial article:

- https://github.com/Createdd/Writing/blob/master/2020/articles/mlApiCovid.md


It paints a picture for developing a machine learning Python API from start to finish and provides help in more difficult areas like the setup with AWS Lambda.

You will find the end result on Rapidapi:

- https://rapidapi.com/Createdd/api/covid_new_cases_prediction

If you found this article helpful let me know and/or buy the functionality on Rapidapi to show support.



## Data

We will use the dataset from https://ourworldindata.org/coronavirus-source-data in csv format.s

## Built With

- Github (Code hosting),
- Anaconda (Dependency and environment management),
- Docker (for possible further usage in microservices)
- Jupyter Notebook (code development and documentation),
- Python (programming language),
- AWS, especiall AWS Lambda and S3(for deployment),
- Rapidapi (market to sell)


# About the author

Daniel is an entrepreneur, software developer and lawyer. His knowledge and interests currently revolve around programming machine learning applications and all its related aspects.

**Connect on:**
- [LinkedIn](https://www.linkedin.com/in/createdd)
- [Github](https://github.com/Createdd)
- [Medium](https://medium.com/@createdd)
- [Twitter](https://twitter.com/_createdd)
- [Instagram](https://www.instagram.com/create.dd/)

---


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

to deypoy

```sh
pip uninstall -r requirements.txt -y
```

```sh
pip install Flask pandas boto3 sklearn zappa
```

```sh
pip install -r requirements_prod.txt
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
- https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507


- https://www.bluematador.com/blog/serverless-in-aws-lambda-vs-fargate aws lambda vs fargate
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html billing alarm
- https://towardsdatascience.com/deploy-machine-learning-pipeline-on-aws-fargate-eb6e1c50507
- https://stackoverflow.com/questions/62941174/how-to-write-load-machine-learning-model-to-from-s3-bucket-through-joblib
- https://ianwhitestone.work/zappa-zip-callbacks/ remove unnecessary files in zappa

zappa issue with pandas https://github.com/Miserlou/Zappa/issues/1927

aws s3

- https://stackabuse.com/file-management-with-aws-s3-python-and-flask/


do not enter name for s3 bucket as it cannot be found

# additional

- https://www.freecodecamp.org/news/what-we-learned-by-serving-machine-learning-models-using-aws-lambda-c70b303404a1/
- https://ianwhitestone.work/slides/serverless-meetup-feb-2020.html
- https://read.iopipe.com/the-right-way-to-do-serverless-in-python-e99535574454