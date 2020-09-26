import boto3
from joblib import load
from botocore.exceptions import NoCredentialsError


def load_model(BUCKET_NAME, MODEL_FILE_NAME, MODEL_LOCAL_PATH):
    s3 = boto3.client('s3')

    try:
        print('Try download')
        s3.download_file(BUCKET_NAME, MODEL_FILE_NAME, MODEL_LOCAL_PATH)
        print("Download Successful")
        rf = load(MODEL_LOCAL_PATH)
        print("Model loading successful")
        return rf
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("Credentials not available")