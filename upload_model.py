import boto3
import os

from botocore.exceptions import NoCredentialsError


# def upload_to_aws(local_file, bucket, s3_file):
#     # s3 = boto3.client('s3')
#     s3 = boto3.client('s3',
#          aws_access_key_id='XXXXX',
#          aws_secret_access_key= 'XXXX')

#     try:
#         s3.upload_file(local_file, bucket, s3_file)
#         print("Upload Successful")
#         return True
#     except FileNotFoundError:
#         print("The file was not found")
#         return False
#     except NoCredentialsError:
#         print("Credentials not available")
#         return False


# uploaded = upload_to_aws('rf_model.joblib', 'ml-api-covid-model', 'rf_model.joblib')

# def uploadDirectory(local_path_to_model, bucketname, s3_dirname = "temp_dir"):
#     """This will connect to the aws and upload our files to S3 bucket.
#     """
#     session = boto3.Session()
#     s3_client = session.client( 's3' )
#     tc = boto3.s3.transfer.TransferConfig()
#     t = boto3.s3.transfer.S3Transfer( client=s3_client, config=tc )

#     for subdir, dirs, files in os.walk(local_path_to_model):
#         for file in files:
#             full_path = os.path.join(subdir, file)
#             with open(full_path, 'rb') as data:
#                 print(full_path, full_path[len(local_path_to_model):])
#                 t.upload_file( full_path, bucketname, s3_dirname + '/'+full_path[len(local_path_to_model):] )


# if __name__ == "__main__":
#     # Change this for selecting bucket (if required)
#     BUCKET = "ml-api-covid-model"
#     # Change the path of the model to upload (if required)
#     local_path_to_model = 'rf_model.joblib'
#     s3_dirname = "model" # S3 bucket folder name
#     uploadDirectory(local_path_to_model, BUCKET, s3_dirname)