import boto3

# terminates newly created instances

# read names of newly created instances from 'instance.txt' file
with open('instance.txt', 'r') as f:
    # ec2_create only creates one instance, so the file only has one line
    instance_id = f.readline()

ec2 = boto3.resource('ec2')

instance = ec2.Instance(instance_id)

# terminate the instance and print the response to the console
response = instance.terminate()
print(response)
