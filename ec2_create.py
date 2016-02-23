import boto3


ec2 = boto3.resource('ec2')

# create ec2 instance from AMI
# Amazon Linux: ami-63b25203
my_instance = ec2.create_instances(
    DryRun=False,
    ImageId='your-ami-id', # use LAMP AMI with instance.php and heartbeat.php endpoints
    MinCount=1,
    MaxCount=1,
    KeyName='your-ssh-key',
    SecurityGroupIds=['your-security-group-id',],
    InstanceType='t2.micro',
    Placement={'AvailabilityZone': 'us-west-2c',},
    Monitoring={'Enabled': False},
)

instance = ec2.Instance(my_instance[0].id)

with open('instance.txt', 'w+') as f:
    f.write(my_instance[0].id)

# wait until the instance is running
instance.wait_until_running()

# register ec2 with load balancer
client = boto3.client('elb')

response = client.register_instances_with_load_balancer(
    LoadBalancerName='web-tier-elb',
    Instances=[
        {
            'InstanceId': my_instance[0].id
        },
    ]
)
