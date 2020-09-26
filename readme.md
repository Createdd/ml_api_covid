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

- [About The Project](#about-the-project)
  - [Data](#data)
  - [Built With](#built-with)
  - [Getting started](#getting-started)
    - [Getting started with development notebooks](#getting-started-with-development-notebooks)
- [About the author](#about-the-author)
- [Remaining ideas:](#remaining-ideas)


# About The Project

This is the API Code for my tutorial article:

- https://github.com/Createdd/Writing/blob/master/2020/articles/mlApiCovid.md


It paints a picture for developing a machine learning Python API from start to finish and provides help in more difficult areas like the setup with AWS Lambda.

You will find the end result on Rapidapi:

- https://rapidapi.com/Createdd/api/covid_new_cases_prediction


## Data

We will use the dataset from https://ourworldindata.org/coronavirus-source-data in csv format.

- License of data is [Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)
- Source code available on [Github](https://github.com/owid/covid-19-data/tree/master/public/data)

## Built With

- Github (Code hosting),
- Anaconda (Dependency and environment management),
- Docker (for possible further usage in microservices)
- Jupyter Notebook (code development and documentation),
- Python (programming language),
- AWS, especiall AWS Lambda and S3(for deployment),
- Rapidapi (market to sell)


## Getting started

```sh
git clone https://github.com/Createdd/ml_api_covid.git
```

```sh
docker build -t ml_api_covid .
```

```sh
docker run -d -p 80:8080 ml_api_covid
```

### Getting started with development notebooks

```sh
git clone https://github.com/Createdd/ml_api_covid.git
```

- Create conda environment `conda create --name NAME python=3.7`
- Register new environment in jupyter `ipython kernel install --name NAME--user`
- Activate conda environment `conda activate PATH_TO_ENVIRONMENT`

```sh
pip install -r requirements.txt
```

Note: If you want to to do exploration with Jypter Notebook you would need to install the Conda environment as the Docker setup only works for the production part (Flask server) of the app.



# About the author

Daniel is an entrepreneur, software developer and lawyer. His knowledge and interests currently revolve around programming machine learning applications and all its related aspects.

**Connect on:**
- [LinkedIn](https://www.linkedin.com/in/createdd)
- [Github](https://github.com/Createdd)
- [Medium](https://medium.com/@createdd)
- [Twitter](https://twitter.com/_createdd)
- [Instagram](https://www.instagram.com/create.dd/)

If this was helpful for you consider showing support:
<a href="https://www.buymeacoffee.com/createdd" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>


---

# Remaining ideas:

- [ ] Create an upload script
- [ ] Create a script for deployment. meaning to
  - [ ] uninstall unused deps
  - [ ] install prod deps
  - [ ] do zappa deploy dev






