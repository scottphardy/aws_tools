#!/usr/bin/env python3

import boto3

region = input('Enter a Region name: ')
ec2 = boto3.resource('ec2', region_name=region)
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

ids = []
for instance in instances:
    ids.append(instance.id)

def stop_instances():
    for instance_id in ids:
        instance = ec2.Instance(instance_id)
        response = instance.stop()

stop_instances()

print('Stopping the following instances: ')
print('\n')
for i in ids:
    id = str(i)
    print(id)
print('\n')