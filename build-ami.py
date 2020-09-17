from __future__ import print_function
import boto3
import io
import subprocess
from packerpy import PackerExecutable
from botocore.exceptions import ClientError

BUCKET_NAME = 'demo-s3lambdas'
download_dir = '/tmp/'
def lambda_handler(event, context):
    
    s3 = boto3.resource('s3')
    s3Client = boto3.client('s3')
    try:
        my_bucket = s3.Bucket(BUCKET_NAME)
        for s3_object in my_bucket.objects.all():
           filename = s3_object.key
           s3Client.download_file(BUCKET_NAME, filename, f'{download_dir}{filename}')
    except ClientError as e:
        return False
    #subprocess.call("ls -lrt /opt/python/lib/python3.8/site-packages/packerpy", shell=True)
    p = PackerExecutable("/opt/python/lib/python3.8/site-packages/packerpy/packer")
    #p.validate(f'{download_dir}ami-packer.json')
    (ret, out, err)=p.build(f'{download_dir}ami-packer.json')
    print(out)
    subprocess.call("ls -lrt /tmp", shell=True)
