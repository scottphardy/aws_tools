#!/usr/bin/env python3

import boto3

region = input('Enter a Region name: ')
ec2 = boto3.resource('ec2', region_name=region)
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

def list_instances():
    for instance in instances:
        print(instance.id, instance.instance_type)

print('\n')
print('The following EC2 instances are running: ')
print('\n')
list_instances()
print('\n')
