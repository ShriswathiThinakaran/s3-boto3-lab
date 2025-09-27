import boto3

# Initialize S3 client
s3 = boto3.client('s3')

#  Bucket names must be globally unique
bucket_name = 'my-boto3-s3-bucket-shris-20250927'

# Create the bucket
response = s3.create_bucket(Bucket=bucket_name)

print(f'Bucket {bucket_name} created successfully!')
