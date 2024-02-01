import boto3

aws_management_console = boto3.session.Session(profile_name="default")
iam_console = aws_management_console.resource('iam') # here we can give any services name 'iam,ec2',


for each_user in iam_console.users.all():
    print(each_user.name)
