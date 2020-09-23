import boto3
from botocore.exceptions import NoCredentialsError


def load_model(BUCKET_NAME, MODEL_FILE_NAME, MODEL_LOCAL_PATH):
    s3 = boto3.client('s3')

    try:
        s3.download_file(BUCKET_NAME, MODEL_FILE_NAME, MODEL_LOCAL_PATH)
        print("Download Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False






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