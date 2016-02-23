import boto3

# print out all running ec2 instances and some information about them

# let's use amazon ec2
ec2 = boto3.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

for instance in instances:
    print("instance id: {0}, instance type: {1}".format(instance.id, instance.instance_type))
