import boto3
SSM_CLIENT = boto3.client('ssm')
EC2_CLIENT = boto3.client('ec2')
def lambda_handler(event, context):
    images = EC2_CLIENT.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values': [
                    'ami-linux-aws-custom-*'
                ]
            },
            
        ],
        
    ).get('Images')

    latest = sorted(images, key=lambda k: k['CreationDate'], reverse=True)[0]

    
    response = SSM_CLIENT.put_parameter(
        Name='/GoldenAMI/Linux/RedHat-7/latest',
        
        Value=latest.get('ImageId'),
        Type='String',
        Overwrite=True
    )

    if type(response['Version']) is int:
        return True
    else:
        return False
