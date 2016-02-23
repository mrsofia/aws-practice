# AWS Practice

Just playing around with Boto3's APIs for Amazon Web Services.

You can use these yourself, but you'll have to make sure that your `~/.aws/` directory has the proper `config` and `credentials` files set up (installing AWS CLI does this for you), and you'll want to read through the files to make sure that you've filled in the placeholders with the proper information.

### Files & their descriptions
| File            | Purpose                                                  |
| --------------- | -------------------------------------------------------- |
| `aws.py`        | Prints running ec2 instances and their id's.             |
| `ec2_create.py` | Creates ec2 instance from an AMI and registers with elb. |
| `terminate.py`  | Terminates the ec2 instance created in ec2_create.py.    |
| `py_search.py`  | Prints all files and folders in current directory.       |
