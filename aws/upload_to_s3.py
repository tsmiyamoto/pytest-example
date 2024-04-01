import boto3


def upload_file_to_s3(bucket_name, file_name, object_name=None):
    """
    S3 にファイルをアップロードする関数。
    """
    if object_name is None:
        object_name = file_name

    s3_client = boto3.client("s3")
    response = s3_client.upload_file(file_name, bucket_name, object_name)

    return response
