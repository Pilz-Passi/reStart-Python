import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='examplebucket991561975914375',
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-2',
    },
)

print(response)
