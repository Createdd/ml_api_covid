FROM python:3.7


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# install system dependencies
RUN apt-get update \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*s

# check our python environment
RUN python3 --version
RUN pip3 --version

# install dependencies
RUN pip install --no-cache-dir --upgrade pip

# set work directory
WORKDIR /app

# copy requirements.txt
COPY ./requirements.txt /app/requirements.txt

# install project requirements
RUN pip3 install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# # Generate pikle file
# WORKDIR /app/ML_Model
# RUN python model.py

# # set work directory
# WORKDIR /app

# set app port
EXPOSE 8080

# ENTRYPOINT [ "python3" ]

# Run app.py when the container launches
# CMD [ "app.py","run","--host","0.0.0.0"]
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]
# CMD [ "env FLASK_APP=app.py FLASK_ENV=development flask run" ]