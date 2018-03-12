#!/usr/bin/env python3

import boto3

region = input('Enter a Region name: ')
ec2 = boto3.resource('ec2', region_name=region)
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

def list_instances():
    instances = ec2.instances.filter(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        return(instance.id)

ids = list_instances().split()

def stop_instances():
    for instance_id in ids:
        instance = ec2.Instance(instance_id)
        response = instance.stop()

stop_instances()
# ec2.instances.filter(InstanceIds=ids).stop()
print('%r is stopping... ' % ids)