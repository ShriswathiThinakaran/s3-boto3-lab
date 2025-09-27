import boto3

# Initialize S3 client
s3 = boto3.client('s3')

bucket_name = 'my-boto3-s3-bucket-shris-20250927'
file_name = 'myfile.txt'

# Delete the file
s3.delete_object(Bucket=bucket_name, Key=file_name)

print(f'File {file_name} deleted successfully!')
