import boto3
SSM_CLIENT = boto3.client('ssm')
EC2_CLIENT = boto3.client('ec2')

IMAGE_MAP = {
    'amzn2-ami-hvm-*-x86_64-gp2':      '/images/amazon/amazon-linux-2',
    'amzn-ami-hvm-*-x86_64-gp2':       '/images/amazon/amazon-linux',
    'amzn-ami-*-amazon-ecs-optimized': '/images/amazon/amazon-linux-ecs',
    'amzn2-ami-ecs-hvm-*-x86_64-ebs':  '/images/amazon/amazon-linux-2-ecs'
}


def lambda_handler(event, context):
    for k, v in IMAGE_MAP.items():
        if __find_and_store_image(k, v) is not True:
            return False
    return True


def __find_and_store_image(name, ssm_param):
    images = EC2_CLIENT.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values': [
                    'ami-linux-aws-custom-1600380960-new'
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
