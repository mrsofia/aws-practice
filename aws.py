import boto3

# print out all running ec2 instances and some information about them

# NOTE: for this to work, you must have the proper credentials and configuration
# in your ~/.aws folder (for UNIX-based systems - you will have to reconfigure
# it yourself for Microsoft).

# let's use amazon ec2
ec2 = boto3.resource('ec2')

# show only 'running' instances. Note this will also grab instances that are
# running, but not passing status checks.
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
)

# print ec2 instance id and type to the console
for instance in instances:
    print("instance id: {0}, instance type: {1}".format(instance.id, instance.instance_type))
