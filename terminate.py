import boto3

with open('instance.txt', 'r') as f:
    instance_id = f.readline()

ec2 = boto3.resource('ec2')

instance = ec2.Instance(instance_id)

response = instance.terminate()
print(response)
