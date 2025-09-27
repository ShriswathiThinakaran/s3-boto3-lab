import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Use your bucket name
bucket_name = 'my-boto3-s3-bucket-shris-20250927'
file_name = 'myfile.txt'

# Create a local file
with open(file_name, 'w', encoding='utf-8') as f:
    f.write("Hello S3")

# Upload file to S3
s3.upload_file(file_name, bucket_name, file_name)

print(f'File {file_name} uploaded successfully!')
