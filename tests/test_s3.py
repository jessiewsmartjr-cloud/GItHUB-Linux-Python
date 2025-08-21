import pytest
from unittest.mock import MagicMock

def test_s3_copy_success():
    s3_client = MagicMock()
    s3_client.copy_object.return_value = {'ResponseMetadata': {'HTTPStatusCode': 200}}
    result = s3_client.copy_object(Bucket='dest', Key='file.txt', CopySource='source/file.txt')
    assert result['ResponseMetadata']['HTTPStatusCode'] == 200
