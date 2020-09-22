import boto3
import os
from joblib import load
from boto.s3.key import Key
from boto.s3.connection import S3Connection

from botocore.client import Config


# s3 = boto3.resource(
#     's3',
#     aws_access_key_id='XXXXXX',
#     aws_secret_access_key='XXXXXXX',
#     config=Config(signature_version='s3v4')
# )


BUCKET_NAME = 'ml-api-covid-model'
MODEL_FILE_NAME = 'rf_model.joblib'
MODEL_LOCAL_PATH = f'{MODEL_FILE_NAME}_downloaded'



def load_model():
    s3 = boto3.client(
        's3',
        # aws_access_key_id='XXXXX',
        # aws_secret_access_key='XXXX',
        # config=Config(signature_version='s3v4')
    )

    # for bucket in s3.buckets.all():
    #     print(bucket.name)

    # Download object at bucket-name with key-name to tmp.txt
    s3.download_file(BUCKET_NAME, MODEL_FILE_NAME, MODEL_LOCAL_PATH)
    print('done')

#   conn = S3Connection()
#   bucket = conn.create_bucket(BUCKET_NAME)
#   key_obj = Key(bucket)
#   key_obj.key = MODEL_FILE_NAME

#   contents = key_obj.get_contents_to_filename(MODEL_LOCAL_PATH)
#   return load(MODEL_LOCAL_PATH)

rf = load_model()



# def download_dir(client, resource, dist, bucket, local='/tmp'):
#     """
#     """
#     paginator = client.get_paginator('list_objects')
#     print(paginator)
#     for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
#         if result.get('CommonPrefixes') is not None:
#             for subdir in result.get('CommonPrefixes'):
#                 download_dir(client, resource, subdir.get('Prefix'), local, bucket)
#         if result.get('Contents') is not None:
#             for file in result.get('Contents'):
#                 if not os.path.exists(os.path.dirname(local + os.sep + file.get('Key'))):
#                      os.makedirs(os.path.dirname(local + os.sep + file.get('Key')))
#                 resource.meta.client.download_file(bucket, file.get('Key'), local + os.sep + file.get('Key'))


# if __name__ == "__main__":
#     boto3.setup_default_session(profile_name='default')
#     client = boto3.client('s3')
#     resource = boto3.resource('s3')
#     download_dir(client, resource, 'model/', "ml-api-covid-model", 'test')