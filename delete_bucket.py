import boto3

# Initialize S3 client
s3 = boto3.client('s3')

bucket_name = 'my-boto3-s3-bucket-shris-20250927'

# Attempt to delete the bucket
s3.delete_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} deleted successfully!')
