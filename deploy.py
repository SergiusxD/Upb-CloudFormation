<<<<<<< HEAD
#!/usr/bin/python3
import getopt, sys

argument_list = sys.argv[1:]
short_options = "cduw"
long_options = ["create", "delete", "update", "website"]

try:
    argument, values = getopt.getopt(argument_list, short_options, long_options)
    command = argument[0][0]
except getopt.error as err:
    print(str(err))
    sys.exit(2)
    
##########################################################################

import boto3
PROJECT = "upb-cloudformation2"
BUCKET_NAME = f"{PROJECT}-bucketbatachi-123"
=======
import boto3

PROJECT = "Upb-CloudFormation"
>>>>>>> 7a44a0f79ce8bbd27f259c174a35e50b142a3679

cf = boto3.client('cloudformation')

with open('template.yaml', 'r') as file:
    template = file.read()
<<<<<<< HEAD
    
if command in("--create","--c"):
    response = cf.create_stack(
        StackName=PROJECT,
        TemplateBody= template,
        Parameters=[
            {
                'ParameterKey': 'BuketName',
                'ParameterValue': BUCKET_NAME
            },
        ]
    )
    print(response)
    

if command in("--update","-u"): 
    response = cf.update_stack(
        StackName=PROJECT,
        TemplateBody= template
    )
    print(response)
    
if command in("--delete","-d"):
    response = cf.delete_stack(StackName=PROJECT)
    print(response)
    
print("done!")
=======

response = cf.create_stack(
    StackName=PROJECT,
    TemplateBody= template
)

print(response)

>>>>>>> 7a44a0f79ce8bbd27f259c174a35e50b142a3679
