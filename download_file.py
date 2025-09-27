import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Use your bucket name
bucket_name = 'my-boto3-s3-bucket-shris-20250927'
file_name = 'myfile.txt'
download_name = 'downloaded-file.txt'

# Download the file
s3.download_file(bucket_name, file_name, download_name)

print(f'File {file_name} downloaded successfully as {download_name}!')
