import boto3

ec2 = boto3.resource('ec2')

# create ec2 instance from AMI
my_instance = ec2.create_instances(
    DryRun=False, # change to True if you are just testing to see if it works.
    ImageId='your-ami-id', # use LAMP AMI with instance.php and heartbeat.php endpoints
    MinCount=1, # minimum number of instances to be spun up
    MaxCount=1, # maximum number of instances to spin up
    KeyName='your-ssh-key', # key generated or assigned when creating instance. doesn't need .pem extension
    SecurityGroupIds=['your-security-group-id',], # adds instance to security group
    InstanceType='t2.micro', # free tier instance
    Placement={'AvailabilityZone': 'us-west-2c',},
    Monitoring={'Enabled': False}, # monitoring costs money
)

# grab reference to our newly-created instance
instance = ec2.Instance(my_instance[0].id)

# write instance id to file
with open('instance.txt', 'w+') as f:
    f.write(my_instance[0].id)

# wait until the instance is running... takes a minute or two
instance.wait_until_running()

# grab elb Service Resource
client = boto3.client('elb')

# register new ec2 instance with load balancer
response = client.register_instances_with_load_balancer(
    LoadBalancerName='your-elb-name',
    Instances=[
        {
            'InstanceId': my_instance[0].id
        },
    ]
)
