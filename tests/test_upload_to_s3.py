import boto3
import pytest
from moto import mock_s3

from aws.upload_to_s3 import upload_file_to_s3


@pytest.fixture
def aws_credentials():
    """AWS 認証情報をモックするフィクスチャ"""
    with mock_s3():
        yield boto3.client("s3", region_name="us-east-1")


@pytest.fixture
def s3_bucket(aws_credentials):
    """S3 バケットを作成するフィクスチャ"""
    client = aws_credentials
    client.create_bucket(Bucket="my-test-bucket")
    yield "my-test-bucket"


def test_upload_file_to_s3(s3_bucket):
    """S3 にファイルをアップロードする関数のテスト"""
    # ファイルをアップロード
    upload_file_to_s3(s3_bucket, "test.txt", "test.txt")

    # アップロードされたファイルが存在することを確認
    client = boto3.client("s3", region_name="us-east-1")
    response = client.list_objects_v2(Bucket=s3_bucket)
    assert "Contents" in response
    filenames = [obj["Key"] for obj in response["Contents"]]
    assert "test.txt" in filenames
